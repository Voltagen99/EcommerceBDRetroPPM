from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'bottega_retrogaming/store.html', context)

def cart(request):
    context = {}
    return render(request, 'bottega_retrogaming/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'bottega_retrogaming/checkout.html', context)
