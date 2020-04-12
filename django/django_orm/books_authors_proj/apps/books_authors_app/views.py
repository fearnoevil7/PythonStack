from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


def index(request, page):
    if page == "authors":
        context = {
            'Author': Author.objects.all(),
            'page': page,
        }
        return render(request, "books_authors_app/index.html",context)
    if page == "books":
        context = {
            'Book': Book.objects.all(),
            'page': page
        }
        return render(request,"books_authors_app/index.html", context)


def description(request, page, id):
    if page == "books":
        context = {
            'Book': Book.objects.get(id=id),
            'authors': Book.objects.get(id=id).authors.all(),
            'page': page,
            'appendAuthor': Author.objects.exclude(books__id=id)
        }
        return render(request, "books_authors_app/desc.html", context)

    if page == "authors":
        context = {
            'Author': Author.objects.get(id=id),
            'Book': Author.objects.get(id=id).books.all(),
            'page': page,
            'appendBook': Book.objects.exclude(authors__id=id)
        }
        return render(request, "books_authors_app/desc.html", context)

def process(request, page):
    if page == "books":
        if request.method == "POST":
            Book.objects.create(title = request.POST["bTitle"], desc = request.POST["bDesc"])
            return redirect('/home'+page)
    if page == "authors":
        if request.method == "POST":
            Author.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], notes = request.POST["notes"])
            return redirect('/home'+page)

def appendProcess(request,page,id):
    if page == "books":
        if request.method == "POST":
            Book.objects.get(id=id).authors.add(Author.objects.get(id=request.POST['authorId']))

    if page == "authors":
        if request.method == "POST":
            Author.objects.get(id=id).books.add(Book.objects.get(id=request.POST['bookId']))

    return redirect('/'+page+'/description/'+id)
