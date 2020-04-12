from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt
def index(request):
    return render(request, 'projectApp/registrationForm.html')
# Create your views here.
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        safeword = request.POST['password']
        pw_hash = bcrypt.hashpw(safeword.encode(), bcrypt.gensalt())
        print(pw_hash)
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        print("Account registered!!!!!!!!*********************!!!!!!")
        return redirect('/')

def login(request):
    member = User.objects.filter(email = request.POST['email'])
    if member:
        logged_user = member[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['memberid'] = logged_user.id
            return redirect('/home')
        else:
            messages.error(request, "invalid password")
            redirect('/')
    else:
        messages.error(request, "invalid email")
        redirect('/')

def home(request):
    if 'memberid' not in request.session:
        return redirect('/')
    else:
        context = {
            'member': User.objects.get(id=request.session['memberid']),
            'memberMessage': Message.objects.all(),
            'memberComment': Comment.objects.all()
        }
        # context['memberMessage'].delete()
        return render(request, 'projectApp/wallHome.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def postMessage(request):
    if request.method == 'POST':
        Message.objects.create(user = User.objects.get(id=request.session['memberid']), message = request.POST['memberMessage'])
        return redirect('/home')

def postComment(request, id):
    if request.method == 'POST':
        Comment.objects.create(message = Message.objects.get(id=id), user = User.objects.get(id=request.session['memberid']), comment = request.POST['memberComment'])
        print("Comment created!!!!!!!!")
        return redirect('/home')