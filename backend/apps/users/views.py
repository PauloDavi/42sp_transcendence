from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usúario não esta logado')
        return redirect('login')

    return render(request, "users/home.html")

def login(request):
    return render(request, "users/login.html")
