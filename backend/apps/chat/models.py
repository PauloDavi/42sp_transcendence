from django.db import models
from apps.users.models import User
import uuid

class Messages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
