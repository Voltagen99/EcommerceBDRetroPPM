import json
from .models import *
from django.db import IntegrityError
from user_management.models import CustomUser

def cookieCart(request):
    try:
        cart_cookie = json.loads(request.COOKIES['cart'])
    except KeyError:
        cart_cookie = {}

    print('Cart:', cart_cookie)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']
    for i in cart_cookie:
        try:
            cartItems += cart_cookie[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart_cookie[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart_cookie[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageUrl': product.imageUrl
                },
                'quantity': cart_cookie[i]['quantity'],
                'get_total': total
            }
            items.append(item)

            if not product.digital:
                order['shipping'] = True
        except Product.DoesNotExist:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user
        try:
            order = Order.objects.get(customer=customer, complete=False)
        except Order.DoesNotExist:
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    print('Utente non loggato, avvio registrazione in-place...')

    name = data['form']['name']
    email = data['form']['email']
    password = data['form']['password']
    password_confirm = data['form']['password-confirm']

    if password != password_confirm:
        return None, {'error': 'Le password non coincidono.'}

    try:
        customer = CustomUser.objects.create_user(
            username=name,
            email=email,
            password=password
        )
    except IntegrityError:
        return None, {'error': 'Username o email già esistenti.'}
    except Exception as e:
        return None, {'error': f'Si è verificato un errore imprevisto: {e}'}

    cookieData = cartData(request)
    items = cookieData['items']
    order = Order.objects.create(
        customer=customer,
        complete=False,
        )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
    return customer, order