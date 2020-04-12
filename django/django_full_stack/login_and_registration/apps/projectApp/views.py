from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
def index(request):
    return render(request, "projectApp/index.html")


def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        print('account registered!!!!!!*********')
        return redirect('/')

def log_in(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/success')
        else:
            messages.error(request, "invalid password")
            return redirect ('/')
    else:
        messages.error(request, "invalid email")
        return redirect ('/')

def success(request):
    if 'user_id' in request.session:
        context = {
            'person': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'projectApp/success.html', context)
    else:
        return redirect('/')

def log_out(request):
    request.session.flush()
    return redirect('/')

def post_message(request):
    
# Create your views here.
