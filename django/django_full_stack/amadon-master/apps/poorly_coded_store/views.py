from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def buy(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST['product_id'])
    price_from_form = product.price
    total_charge = quantity_from_form * price_from_form
    print(Order.objects.all().values)
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')

def checkout(request):
    context = {
        'orders': Order.objects.last(),
        'numberOfItems': len(Order.objects.all()),
        'total': Order.objects.aggregate(Sum('total_price'))['total_price__sum'],
    }
    return render(request, 'store/checkout.html', context)