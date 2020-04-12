from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Thought
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
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        print(new_user.first_name)
        print(new_user.last_name)
        return redirect('/')

def home_dashboard(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        thoughts = Thought.objects.all()
        context = {
            'user': user,
            'thoughts': thoughts,
            # 'numLikes': len(thoughts.users_that_like.all())
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
            user = User.objects.filter(email=request.POST['email'])
            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['user_id'] = logged_user.id
                    return redirect('/home_dashboard')
                else:
                    return redirect('/')
    return redirect('/')
def logout(request):
    request.session.flush()
    return redirect('/')

def create_thought(request, id):
    errors = Thought.objects.thought_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home_dashboard')
    else:
        new_thought=Thought.objects.create(thought = request.POST['thought'], created_by = User.objects.get(id=id))
        new_thought.users_that_like.add(User.objects.get(id=id))
        print(new_thought.thought)
        print(new_thought.created_by.first_name)
        return redirect('/home_dashboard')
    return redirect('/home_dashboard')

def thought_desc(request, thought_id, user_id):
    if 'user_id' in request.session:
        user = User.objects.get(id=user_id)
        thought = Thought.objects.get(id=thought_id)
        context = {
            'member': user,
            'thought': thought,
            'users_that_like': thought.users_that_like.all(),
            'user_in': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "projectApp/description.html", context)
    else:
        return redirect('/')

def addLike(request, thought_id, user_id):
    the_thought = Thought.objects.get(id=thought_id)
    user = User.objects.get(id=user_id)
    the_thought.users_that_like.add(user)
    members = the_thought.users_that_like
    print(members.all())
    return redirect("/thought_desc/"+thought_id+"/"+user_id)

def unlike(request, thought_id, user_id):
    thought = Thought.objects.get(id=thought_id)
    user = User.objects.get(id=user_id)
    thought.users_that_like.remove(user)
    members = thought.users_that_like
    print(members.all())
    return redirect("/thought_desc/"+thought_id+"/"+user_id)

def delete(request, thought_id, user_id):
    thought = Thought.objects.get(id=thought_id)
    user = User.objects.get(id=user_id)
    if thought.created_by.id == user.id:
        thought.delete()
        return redirect("/home_dashboard")
    else:
        return redirect("/home_dashboard")

# Create your views here.
