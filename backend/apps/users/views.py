from django.shortcuts import render, redirect
from django.contrib import auth
from apps.users.forms import UserLoginForm, UserCreationForm, ChatForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "users/home.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, "Usuário criado com sucesso")
            return redirect("home")

    return render(request, "users/register.html", { "form": form })

def login(request):
    if request.user.is_authenticated:
        return redirect("home")

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
                messages.success(request, "Login realizado com sucesso")
                return redirect("home")
            
            messages.error(request, "Usuário ou senha inválidos")
            return redirect("login")

    return render(request, "users/login.html", { "form": form })

@login_required
def chat(request):
    form = ChatForm()
    if request.method == "POST":
        form = ChatForm(request.POST)

    return render(request, "users/chat.html", { "form": form })

def logout(request):
    messages.success(request, "Usuário deslogado com sucesso")
    auth.logout(request)
    return redirect("login")
