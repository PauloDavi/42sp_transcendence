from django.urls import path
from apps.chat.views import index, room


urlpatterns = [
    path("index", index, name="chat_index"),
    path("<str:room_name>/", room, name="room"),
]
