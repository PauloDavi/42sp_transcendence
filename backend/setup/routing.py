from django.urls import re_path
from apps.matchmaking.consumers import OnlineStatusConsumer

websocket_urlpatterns = [
    re_path(r"ws/online-status/$", OnlineStatusConsumer.as_asgi()),
]
