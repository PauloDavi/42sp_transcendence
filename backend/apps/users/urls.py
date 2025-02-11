from django.contrib import admin
from django.urls import path
from apps.users.views import home, login, register, logout, chat

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("chat", chat, name="chat"),
    path("logout", logout, name="logout"),
]
