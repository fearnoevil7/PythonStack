from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    request.session['inc'] = 0
    if 'amount' not in request.session:
        request.session['amount'] = 0
    return render(request, "NinjaGoldApp/index.html")

def transactions(request):
    if request.method == "POST":
        request.session['building'] = request.POST['facility']
        if request.session['building'] == 'farm':
            print(request.session['building'])
            cashflow = random.randrange(0,21)
            request.session['amount'] += cashflow
        if request.session['building'] == 'cave':
            cashflow = random.randrange(5,11)
            request.session['amount'] += cashflow
        if request.session['building'] == 'house':
            cashflow = random.randrange(2,6)
            request.session['amount'] += cashflow
        if request.session['building'] == 'casino':
            cashflow = random.randrange(-50,50)
            request.session['amount'] += cashflow
        return redirect('/')
    # else:
    #     request.session['amount'] += 5

def clear(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
