from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Campi Personalizzati', {'fields': ('user_type', 'name')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campi Personalizzati', {'fields': ('user_type', 'name')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)