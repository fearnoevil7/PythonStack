from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, "projectApp/index.html")
# Create your views here.
