from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
def index(request, page):
    if page == 'books':
        context = {
            'Book': Book.objects.all(),
            'page': page
        }
        return render(request, "projectApp/index.html", context)
    if page == 'authors':
        context = {
            'Author': Author.objects.all(),
            'page': page
        }
        return render(request, "projectApp/index.html", context)

def process(request, page):
    if page == 'books':
        if request.method == 'POST':
            Book.objects.create(title=request.POST['bookTitle'], description=request.POST['bookDescription'])
            return redirect('/home'+page)
    
    if page == 'authors':
        if request.method == 'POST':
            Author.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], notes = request.POST['notes'])
            return redirect('/home'+page)

def description(request, page, id):
    if page == 'books':
        context = {
            'Book': Book.objects.get(id=id),
            'page': page,
            'Authors': Book.objects.get(id=id).authors.all(),
            'otherAuthors': Author.objects.exclude(books__id = id)
        }
        return render(request, "projectApp/desc.html",context)
    if page == 'authors':
        context = {
            'Author': Author.objects.get(id=id),
            'page': page,
            'Books': Author.objects.get(id=id).books.all(),
            'otherBooks': Book.objects.exclude(authors__id = id)
        }
        return render(request, "projectApp/desc.html",context)

def append(request, page, id):
    if page == 'books':
        if request.method == 'POST':
            Book.objects.get(id=id).authors.add(Author.objects.get(id=request.POST['otroAuthor']))
            return redirect('/'+page+'/description/'+id)

    if page == 'authors':
        if request.method == 'POST':
            Author.objects.get(id=id).books.add(Book.objects.get(id=request.POST['otherLibros']))
            return redirect('/'+page+'/description/'+id)
# Create your views here.
