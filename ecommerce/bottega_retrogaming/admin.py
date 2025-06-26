from django.contrib import admin
from .models import Product, Order, OrderItem, ShippingAddress

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered', 'complete')
    list_filter = ('complete', 'date_ordered')

admin.site.register(Order, OrderAdmin)
