from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import ContextMixin

from bottega_retrogaming.models import Product, Order, OrderItem, ShippingAddress
from .forms import ProductForm, OrderForm, OrderItemForm, ShippingAddressForm
from bottega_retrogaming.utils import cartData

class AdminRequiredMixin(UserPassesTestMixin, ContextMixin):
    request: HttpRequest
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'ADMIN'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = cartData(self.request)
        context['cartItems'] = data.get('cartItems', 0)
        return context

class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'manager_view/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = Product.objects.count()
        context['order_count'] = Order.objects.count()
        context['orderitem_count'] = OrderItem.objects.count()
        context['shippingaddress_count'] = ShippingAddress.objects.count()
        return context

# Viste per Product
class ProductListView(AdminRequiredMixin, ListView):
    model = Product
    template_name = 'manager_view/product_list.html'
    context_object_name = 'products'

class ProductCreateView(AdminRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:product_list')

class ProductUpdateView(AdminRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:product_list')

class ProductDeleteView(AdminRequiredMixin, DeleteView):
    model = Product
    template_name = 'manager_view/confirm_delete.html'
    success_url = reverse_lazy('manager_view:product_list')

# Viste per Order
class OrderListView(AdminRequiredMixin, ListView):
    model = Order
    template_name = 'manager_view/order_list.html'
    context_object_name = 'orders'

class OrderCreateView(AdminRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:order_list')

class OrderUpdateView(AdminRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:order_list')

class OrderDeleteView(AdminRequiredMixin, DeleteView):
    model = Order
    template_name = 'manager_view/confirm_delete.html'
    success_url = reverse_lazy('manager_view:order_list')

# Viste per OrderItem
class OrderItemListView(AdminRequiredMixin, ListView):
    model = OrderItem
    template_name = 'manager_view/orderitem_list.html'
    context_object_name = 'orderitems'

class OrderItemCreateView(AdminRequiredMixin, CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:orderitem_list')

class OrderItemUpdateView(AdminRequiredMixin, UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:orderitem_list')

class OrderItemDeleteView(AdminRequiredMixin, DeleteView):
    model = OrderItem
    template_name = 'manager_view/confirm_delete.html'
    success_url = reverse_lazy('manager_view:orderitem_list')

# Viste per ShippingAddress
class ShippingAddressListView(AdminRequiredMixin, ListView):
    model = ShippingAddress
    template_name = 'manager_view/shippingaddress_list.html'
    context_object_name = 'shippingaddresses'

class ShippingAddressCreateView(AdminRequiredMixin, CreateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:shippingaddress_list')

class ShippingAddressUpdateView(AdminRequiredMixin, UpdateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'manager_view/form.html'
    success_url = reverse_lazy('manager_view:shippingaddress_list')

class ShippingAddressDeleteView(AdminRequiredMixin, DeleteView):
    model = ShippingAddress
    template_name = 'manager_view/confirm_delete.html'
    success_url = reverse_lazy('manager_view:shippingaddress_list')