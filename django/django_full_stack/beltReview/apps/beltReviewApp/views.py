from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
import bcrypt
def index(request):
    return render(request, "beltReviewApp/index.html")


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], alias = request.POST['alias'], email = request.POST['email'], password = pw_hash)
        print("User created********")
        print(User.objects.all())
        return redirect('/')

def user_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'member': User.objects.get(id=request.session['user_id']),
            'bookReviews': Review.objects.all().order_by("-id")[:3],
            'books': Book.objects.all()
        }
        return render(request, "beltReviewApp/userDashboard.html",context)

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/user_dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def addHome(request, id):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "beltReviewApp/addHome.html", context)

def bookDesc(request, id):
    book = Book.objects.get(id=id)
    # my_review = Review.objects.get(id=request.session['review_id'])
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'book': book,
        'bookRev': book.reviews.order_by("-id")[:3],
        'poster_id': request.session['user_id']
    }
    return render(request, "beltReviewApp/bookDescription.html", context)

def add(request):
    print(request.POST)
    if request.POST['author'] == "":
        creator = request.POST['dropDownAuthor']
        pass
    else:
        creator = request.POST['author']
    print(request.POST['author'] == "")
    print (creator)
    new_book = Book.objects.create(user = User.objects.get(id = request.session['user_id']), title = request.POST['title'], author = creator)
    Review.objects.create(user = User.objects.get(id = request.session['user_id']), book = Book.objects.get(id = new_book.id), review = request.POST['review'])
    print("book created******")
    print(Review.objects.all())
    print(Book.objects.all())
    # return redirect('/')
    return redirect('/bookDesc/' + str(new_book.id))

def userDesc(request, id):
    member = User.objects.get(id=id)
    context = {
        'member': member,
        'reviewCount': len(Review.objects.filter(user=id)),
        'reviews': member.reviews.all() 
        # list of books with reviews from the user
    }
    return render(request, "beltReviewApp/userDescription.html", context)


def addReview(request,id):
    newReview = Review.objects.create(user = User.objects.get(id = request.session['user_id']), book = Book.objects.get(id=id), review = request.POST['thereview'])
    Book.objects.get(id=id).reviews.add(newReview)
    print(request.POST)
    print(newReview)
    print("review created********")

    return redirect('/bookDesc/' + id)
# Create your views here.

def deleteReview(request, review_id, user_id, book_id):
    if user_id == request.session['user_id']:
        deleteReview = Review.objects.get(id=review_id)
        deleteReview.delete()
        return redirect('/bookDesc/' + book_id)
    else:
        return redirect('/bookDesc/' + book_id)