from django.contrib import admin
from django.urls import path
from apps.users.views import home, login, logout, register, update_user, chat

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("register", register, name="register"),
    path("user/edit", update_user, name="update_user"),
    path("chat", chat, name="chat"),
]
