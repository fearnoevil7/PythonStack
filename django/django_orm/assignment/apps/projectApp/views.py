from django.shortcuts import render, redirect
from django.contrib import messages

from .models import tvShow
def index(request):
    context = {
        'show': tvShow.objects.all(),
    }
    return render(request, 'projectApp/index.html', context)

def configure(request):
    # if configuration == 'add':
    #     context = {
    #         'configuration': configuration
    #     }
    return render(request, ('projectApp/add.html'))

def add(request):
    errors = tvShow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/configure')
    else:
        if request.method == 'POST':
            context = {
                'newShow': tvShow.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], description = request.POST['description'])
            }
            return redirect('/', context)

def delete(request, id):
    if request.method == 'GET':
        context = {
            'delete': tvShow.objects.get(id=id).delete()
        }
        return redirect('/', context)

def edit(request, id):
    context = {
        'edit': tvShow.objects.get(id=id)
    }
    return render(request, 'projectApp/edit.html', context)

def update(request, id):
    errors = tvShow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+id)
    else:
        if request.method == 'POST':
            change = tvShow.objects.get(id=id)
            change.title = request.POST['title']
            change.network = request.POST['network']
            change.release_date = request.POST['release_date']
            change.description = request.POST['description']
            change.save()
            return redirect('/')

def show(request, id):
    if request.method == 'GET':
        context = {
            'show': tvShow.objects.get(id=id),
        }
    return render(request, 'projectApp/show.html', context)
# Create your views here.
