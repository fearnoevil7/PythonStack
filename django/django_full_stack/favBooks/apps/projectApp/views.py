from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt
def index(request):
    return render(request, ("projectApp/index.html"))

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        safeword = request.POST['password']
        pw_hash = bcrypt.hashpw(safeword.encode(), bcrypt.gensalt())
        print(pw_hash)
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        print('Account created!!!!!!!********')
        print(new_user.first_name)
        return redirect('/')

def home_dashboard(request):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        books = Book.objects.all()
        # booketc = books.users_who_like.get(id=user.id)
        context = {
            'member': user,
            'books': books,
            # 'all_liked_books':user.liked_books.filter(users_who_like = user),
            'all_liked_books': Book.objects.filter(users_who_like = user),
            'unliked_books':Book.objects.exclude(users_who_like=user),
        }
        return render(request, "projectApp/add.html", context)
    else:
        return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/home_dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def addBook(request, id):
    errors = Book.objects.addValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/home_dashboard')
    else:
        added_book = Book.objects.create(title = request.POST['title'], uploaded_by = User.objects.get(id=id), description = request.POST['description'])
        added_book.users_who_like.add(User.objects.get(id=id))
        print(added_book.title)
        print(added_book.description)
        print(added_book.users_who_like.all().values())
        return redirect('/home_dashboard')

def bookDesc(request, book_id, user_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    # specific = user.liked_books.get(id=book_id)
    # specific = book.users_who_like.get(id=user_id)
    context = {
        'member': user,
        'book': book,
        'users_that_like': book.users_who_like.all(),
        'u': book.users_who_like.filter(id=user_id),
        'q': book.users_who_like.exclude(id=user_id),
        'person': User.objects.get(id=request.session['user_id']),
        'p': User.objects.filter(liked_books=Book.objects.get(id=book_id)),
        'y': User.objects.exclude(liked_books=Book.objects.get(id=book_id)),
    }
    return render(request, "projectApp/bookDescription.html", context)

def update(request, book_id, id):
    errors = Book.objects.addValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/bookDesc/'+book_id+"/"+id)
    else:
        change = Book.objects.get(id=book_id)
        print(change.title)
        change.title = request.POST['title']
        change.description = request.POST['description']
        change.save()
        return redirect('/bookDesc/' + book_id +"/"+ id)

def deleteDesc(request, book_id, id):
    deleteBook = Book.objects.get(id = book_id)
    deleteBook.delete()
    return redirect('/home_dashboard')

def addFav(request, book_id, id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=id)
    book.users_who_like.add(user)
    return redirect('/bookDesc/'+book_id+"/"+id)

def removeFav(request, book_id, id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=id)
    book.users_who_like.remove(user)
    return redirect('/bookDesc/'+book_id+"/"+id)


def userList(request, member_id):
    user = User.objects.get(id=member_id)
    context = {
        'user': user,
        'list': user.liked_books.all()
    }
    return render(request, "projectApp/listOfFavs.html", context)