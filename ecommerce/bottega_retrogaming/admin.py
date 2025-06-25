from django.contrib import admin
from .models import Product, Order, OrderItem, ShippingAddress
from user_management.models import CustomUser

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class OrderAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "customer":
            kwargs["queryset"] = CustomUser.objects.filter(user_type=CustomUser.CUSTOMER)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('id', 'customer', 'date_ordered', 'complete')
    list_filter = ('complete', 'date_ordered')

admin.site.register(Order, OrderAdmin)
