from django.urls import path
from . import views

app_name = 'manager_view'

urlpatterns = [
    path('', views.AdminDashboardView.as_view(), name='admin_dashboard'),

    # URL per i Prodotti
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # URL per gli Ordini
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/add/', views.OrderCreateView.as_view(), name='order_add'),
    path('orders/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    # URL per gli OrderItem
    path('orderitems/', views.OrderItemListView.as_view(), name='orderitem_list'),
    path('orderitems/add/', views.OrderItemCreateView.as_view(), name='orderitem_add'),
    path('orderitems/<int:pk>/edit/', views.OrderItemUpdateView.as_view(), name='orderitem_edit'),
    path('orderitems/<int:pk>/delete/', views.OrderItemDeleteView.as_view(), name='orderitem_delete'),

    # URL per gli Indirizzi di Spedizione
    path('shippingaddresses/', views.ShippingAddressListView.as_view(), name='shippingaddress_list'),
    path('shippingaddresses/add/', views.ShippingAddressCreateView.as_view(), name='shippingaddress_add'),
    path('shippingaddresses/<int:pk>/edit/', views.ShippingAddressUpdateView.as_view(), name='shippingaddress_edit'),
    path('shippingaddresses/<int:pk>/delete/', views.ShippingAddressDeleteView.as_view(), name='shippingaddress_delete'),
]