from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth import login
from django.db.models.functions import Lower
from .models import *
from .utils import guestOrder, cartData
import json
import datetime

class StoreView(ListView):
    model = Product
    template_name = 'bottega_retrogaming/store.html'
    context_object_name = 'products'

    def get_queryset(self):
        """
        Questo metodo applica il filtraggio e l'ordinamento dei prodotti
        """
        queryset = super().get_queryset().order_by()

        sort_option = self.request.GET.get('sort', 'default')
        digital_filter = self.request.GET.get('digital', '')

        if digital_filter == 'yes':
            queryset = queryset.filter(digital=True)
        elif digital_filter == 'no':
            queryset = queryset.filter(digital=False)

        if sort_option == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_option == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort_option == 'name_asc':
            queryset = queryset.order_by(Lower('name'))
        elif sort_option == 'name_desc':
            queryset = queryset.order_by(Lower('name').desc())
        else: # Ordinamento di default per ID
            queryset = queryset.order_by('id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = cartData(self.request)
        context['cartItems'] = data['cartItems']
        return context


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'bottega_retrogaming/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'bottega_retrogaming/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order_or_error = guestOrder(request, data)
        if customer is None:
            return JsonResponse(order_or_error, status=400)
        login(request, customer)
        order = order_or_error

    if order.get_cart_items == 0:
        return JsonResponse({'error': 'Il carrello non può essere vuoto'}, status=400)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )
    else:
        print('No shipping address provided')

    # Aggiorna la data dell'ordine se l'ordine è completo, per farla coincidere con il momento del pagamento
    if order.complete:
        Order.objects.filter(pk=order.pk).update(date_ordered=datetime.datetime.now())
    return JsonResponse('Payment submitted', safe=False)

def product_detail(request, pk):
    data = cartData(request)
    cartItems = data['cartItems']
    product = Product.objects.get(id=pk)
    context = {'product': product, 'cartItems': cartItems}
    return render(request, 'bottega_retrogaming/product.html', context)
