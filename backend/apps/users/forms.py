from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from apps.users.models import User

class UserLoginForm(forms.Form):
  name = forms.CharField(
    label="Nome de login",
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
    label="Sua senha",
    required=True,
    max_length=100,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    ),
  )

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        labels = {
          "username": "Nome de usuário",
          "email": "E-mail",
          "password1": "Senha",
          "password2": "Confirme sua senha",
        }
        
        widgets = {
          "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: João Silva"}),
          "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: joao@silva.com"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, placeholder in {"password1": "Crie uma senha", "password2": "Confirme sua senha"}.items():
            self.fields[field_name].widget.attrs.update({
                "class": "form-control",
                "placeholder": placeholder,
            })

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password"]

class ChatForm(forms.Form):
    content = forms.CharField(
        label="Sua mensagem",
        required=True
    )
