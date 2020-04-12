from django.shortcuts import render, redirect
from .forms import RegistrationForm
def index(request):
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "miniRegisterApp/miniRegister.html", context)

def register(request):
    if request.method == 'POST':
        submittedForm = RegistrationForm(request.POST)
        print(submittedForm.is_valid())
        print(submittedForm.errors)
        return redirect('/')

def make_messages(request):

    ]
# Create your views here.
