from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    context = {
        "random": get_random_string(length= 14)
    }
    if 'count' not in request.session:
        request.session['count'] =1 
    else:
        request.session['count'] += 1
    return render(request, "projectApp/index.html", context)

def destroy(request):
    request.session.flush()
    return redirect('/')