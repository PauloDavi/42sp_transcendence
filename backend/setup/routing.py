from django.urls import re_path
from apps.matchmaking.consumers import OnlineStatusConsumer
from apps.chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/online-status/$", OnlineStatusConsumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
]
