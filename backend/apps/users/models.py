import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=255,
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to="avatars/",
        default="avatars/blank-profile-picture.png"
    )
    status_online = models.BooleanField(default=False)
    wins = models.IntegerField(default=0, verbose_name=_("Vitórias"))
    losses = models.IntegerField(default=0, verbose_name=_("Derrotas"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Criado em"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Atualizado em"))
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password"]
    
    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self):
        return self.username

class Messages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
