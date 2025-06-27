from django.urls import path
from .views import StoreView, cart, checkout, updateItem, processOrder, product_detail

urlpatterns = [
    path('', StoreView.as_view(), name="store"),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
    path('process_order/', processOrder, name="process_order"),
]
