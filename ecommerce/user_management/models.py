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