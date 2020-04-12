from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt
def index(request):
    return render(request, "beltReviewApp/index.html")

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
        User.objects.create(first_name = request.POST['first_name'], last_name= request.POST['last_name'] , alias = request.POST['alias'], email = request.POST['email'], password = pw_hash)
        print("Account Created!!!!!!!*********")
        return redirect('/')

def home_dashboard(request):
    if 'userid' not in request.session:
        return redirect('/')
    else:
        member = User.objects.get(id=request.session['userid'])
        context = {
            'member': member,
            'recent_reviews': member.review.order_by('-id')[:3]
        }
        return render(request, ("beltReviewApp/home_dashboard.html"), context)

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/home_dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def addHome(request, id):
    return render(request, ('beltReviewApp/addBook.html'))

def bookDescription(request, id):
    context = {
        'book': Book.objects.get(id=id)
    }
    return render(request, ("beltReviewApp/bookDescription.html"), context)

def addBook(request):
    if request.method == 'POST':
        new_book = Book.objects.create( user = User.objects.get(id = request.session['userid']), title = request.POST['title'], author = request.POST['addAuthor'], review = request.POST['review'])
        print("Book created!!!!!!!*********")
        print(Book.title)
        print(Book.author)
        print(Book.review)
        return redirect ('/bookDescription/' + str(new_book.id))