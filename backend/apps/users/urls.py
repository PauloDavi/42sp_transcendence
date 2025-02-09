from django.contrib import admin
from django.urls import path
from apps.users.views import home, login, register

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path("register", register, name="register"),
]
