from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            user = self.scope["user"]
            await update_status_online(user, True)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.scope["user"].is_authenticated:
            user = self.scope["user"]
            await update_status_online(user, False)

@database_sync_to_async
def update_status_online(user, status_online):
    user.status_online = status_online
    user.save()
