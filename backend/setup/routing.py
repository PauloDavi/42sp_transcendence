from django.urls import re_path
from setup.consumers import OnlineStatusConsumer

websocket_urlpatterns = [
    re_path(r"ws/online-status/$", OnlineStatusConsumer.as_asgi()),
]
