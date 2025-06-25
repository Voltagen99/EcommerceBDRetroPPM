import json
from .models import *
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
    print('User is not logged in...')
    # Estrai 'name' e 'email' dal form
    name = data['form']['name']
    email = data['form']['email']

    # 1. Controlla se un utente con questo USERNAME (preso dal campo 'name') esiste già
    if CustomUser.objects.filter(username=name).exists():
        print(f"Username '{name}' already exists. Purchase blocked for guest.")
        # 2. Ritorna None per segnalare l'errore alla vista
        return None, None

    # 3. Se l'username è disponibile, crea il nuovo utente
    print(f"Username '{name}' is available, creating new guest account...")
    cookieData = cookieCart(request)
    items = cookieData['items']

    customer = CustomUser.objects.create(
        username=name,  # Imposta l'username
        email=email,  # Imposta l'email
        name=name  # Imposta anche il campo 'name' per visualizzazione
    )

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )

    return customer, order