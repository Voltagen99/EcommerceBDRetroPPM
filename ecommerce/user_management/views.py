from django.shortcuts import redirect
from django.contrib.auth import login
from .models import CustomUser
from django.contrib import messages
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Le password non coincidono.")
            return redirect('login')

        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, f"Registrazione completata! Benvenuto, {user.username}.")
            return redirect('store')
        except IntegrityError:
            messages.error(request, "Username o email già esistenti.")
            return redirect('login')

    return redirect('login')