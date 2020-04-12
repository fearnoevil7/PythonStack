from django.shortcuts import render, redirect
from .models import *
def index(request):
    context = {
        'User': User.objects.all()
    }
    return render(request, "projectApp/index.html", context)

def add_user(request):
    if request.method == "POST": 
        User.objects.create(first= request.POST['first'], last=request.POST['last'], email=request.POST['email'], age=int(request.POST['age']))
    return redirect('/')        

# Create your views here.
