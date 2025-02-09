from django.shortcuts import render, redirect
from django.contrib import auth
from apps.users.forms import UserLoginForm, CustomUserCreationForm, ChatForm
from apps.users.models import Messages

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "users/home.html")

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("home")

    return render(request, "users/register.html", { "form": form })

def login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(
                request,
                username=name,
                password=password,
            )

            if user is not None:
                auth.login(request, user)
                return redirect("home")

            return redirect("login")

    return render(request, "users/login.html", { "form": form })

def chat(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = ChatForm()
    if request.method == "POST":
        form = ChatForm(request.POST)


    return render(request, "users/chat.html", { "form": form })
