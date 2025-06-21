from django.shortcuts import render

def store(request):
    context = {}
    return render(request, 'bottega_retrogaming/store.html', context)

def cart(request):
    context = {}
    return render(request, 'bottega_retrogaming/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'bottega_retrogaming/checkout.html', context)
