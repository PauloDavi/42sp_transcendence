from django import forms

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
