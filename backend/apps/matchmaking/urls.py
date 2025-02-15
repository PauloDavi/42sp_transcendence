from django.urls import path
from apps.matchmaking.views import create_match

urlpatterns = [
    path("create/<uuid:opponent_id>", create_match, name="add_match"),
]
