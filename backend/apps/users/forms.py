from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User

class UserLoginForm(forms.Form):
  name = forms.CharField(
    label='Nome de login',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex: João Silva"
      }
    ),
  )
  password = forms.CharField(
    label='Sua senha',
    required=True,
    max_length=100,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    ),
  )

class CustomUserCreationForm(UserCreationForm):
    password_confirm = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]


class ChatForm(forms.Form):
  content = forms.CharField(
    label='Sua mensagem',
    required=True
    )
