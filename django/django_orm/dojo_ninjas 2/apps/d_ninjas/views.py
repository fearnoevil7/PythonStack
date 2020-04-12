from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context ={
        'Dojo': Dojo.objects.all(),
        'Ninja': Ninja.objects.all()
    }
    return render(request, 'd_ninjas/index.html', context)

def process(request):
    if request.method == "POST":
        Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def add_ninja(request):
    if request.method == "POST":
        Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojos = Dojo.objects.get(id=request.POST['the_dojo'])) 
    return redirect('/')