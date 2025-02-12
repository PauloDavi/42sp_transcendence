from django.shortcuts import render, redirect
from django.contrib import auth
from apps.users.forms import UserLoginForm, UserCreationForm, UserEditProfileForm, ChatForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

@login_required
def home(request):
    return render(request, "users/home.html")

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
                messages.success(request, _("Login realizado com sucesso"))
                return redirect("home")
            
            messages.error(request, _("Usuário ou senha inválidos"))
            return redirect("login")

    return render(request, "users/login.html", { "form": form })

def logout(request):
    messages.success(request, _("Usuário deslogado com sucesso"))
    auth.logout(request)
    return redirect("login")

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, _("Usuário criado com sucesso"))
            return redirect("home")

    return render(request, "users/register.html", { "form": form })

@login_required
def update_user(request):
    if request.method == "POST":
        form = UserEditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, _("Seu perfil foi atualizado com sucesso!"))
            return redirect("home")
    else:
        print(request.user.avatar)
        initial_data = {
            "email": request.user.email,
            "avatar": request.user.avatar,
        }
        form = UserEditProfileForm(initial=initial_data)

    return render(request, "users/update_user.html", { "form": form })

@login_required
def chat(request):
    form = ChatForm()
    if request.method == "POST":
        form = ChatForm(request.POST)

    return render(request, "users/chat.html", { "form": form })
