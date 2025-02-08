from django.contrib import admin
from django.urls import path
from apps.users.views import home, login

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
]
