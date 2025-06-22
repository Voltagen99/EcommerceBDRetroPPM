from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER
    )
    name = models.CharField("Nome visualizzato", max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_staff = True
            self.user_type = self.ADMIN
        else:
            if self.user_type == self.ADMIN:
                self.is_staff = True
            else:
                self.is_staff = False
        super().save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return self.name
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
