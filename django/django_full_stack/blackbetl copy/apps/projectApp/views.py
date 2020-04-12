from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Item
import bcrypt
def index(request):
    return render(request, "projectApp/index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)
        new_user = User.objects.create(name = request.POST['name'], username=request.POST['username'], password=pw_hash)
        print(new_user.name)
        print(new_user.username)
        print("Account registered!!!!!!*********")
        return redirect('/')
    return redirect('/')

def home_dashboard(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'everyone': User.objects.all(),
            'member': User.objects.get(id=request.session['user_id']),
            'likedItems':user.liked_items.all().order_by("updated_at")
        }
        return render(request, "projectApp/home.html", context)
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.filter(username=request.POST['username'])
            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['user_id'] = logged_user.id
                    return redirect('/home_dashboard')
                else:
                    messages.error(request, "Incorrect Password or Username")
                    return redirect('/')
            else:
                messages.error(request, "Incorrect Password or Username")
                return redirect('/')
    else:
        return redirect("/")

def logout(request):
    request.session.flush()
    return redirect('/')

def addHome(request, user_id):
    if 'user_id' in request.session:
        member = User.objects.get(id=user_id)
        context = {
            'member':member,
        }
        return render(request, ("projectApp/add.html"), context)
    else:
        return redirect('/')

def add(request, user_id):
    errors = Item.objects.thought_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/addHome/'+user_id)
    else:
        new_item = Item.objects.create(item = request.POST['item'], added_by = User.objects.get(id=request.session['user_id']))
        request.session['item_id'] = new_item.id
        print(new_item.item)
        print(new_item.added_by)
        print(request.session['item_id'])
        return redirect('/wishList/'+user_id)
def wishList(request, user_id):
    user = User.objects.get(id=user_id)
    item = Item.objects.get(id=request.session['item_id'])
    item.users_that_like.add(user)
    print(item.users_that_like)
    return redirect('/home_dashboard')

def addWish(request, item_id, user_id):
    user = User.objects.get(id=user_id)
    item = Item.objects.get(id=item_id)
    item.users_that_like.add(user)
    return redirect('/home_dashboard')

def removeWish(request, item_id, user_id):
    user = User.objects.get(id=user_id)
    item = Item.objects.get(id=item_id)
    item.users_that_like.remove(user)
    return redirect("/home_dashboard")

def delete(request, item_id, user_id):
    item = Item.objects.get(id = item_id)
    user = User.objects.get(id=user_id)
    if User.objects.get(id=request.session['user_id']) == user:
        if item.added_by.id == User.objects.get(id=request.session['user_id']).id:
            item.delete()
            return redirect("/home_dashboard")
        else:
            return redirect("/")
    else:
        return redirect("/")

def descHome(request, item_id, user_id):
    if 'user_id' in request.session:
        user = User.objects.get(id=user_id)
        item = Item.objects.get(id=item_id)
        context = {
            'user': user,
            'item': item,
            'fans': item.users_that_like.all(),
        }
        return render(request, "projectApp/description.html", context)
    else:
        return redirect('/')
