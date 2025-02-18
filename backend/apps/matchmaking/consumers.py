import json
from django.utils.timezone import now
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from apps.matchmaking.models import Match

User = get_user_model()

class PongConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.match_id = self.scope["url_route"]["kwargs"]["match_id"]
        self.room_group_name = f"match_{self.match_id}"
        self.user = self.scope["user"]

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get("event")

        if event_type == "update_paddle":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "update_paddle",
                    "user_id": str(self.user.id),
                    "position": data["position"],
                }
            )
        elif event_type == "update_score":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "update_score",
                    "right_score": data["right_score"],
                    "left_score": data["left_score"],
                }
            )
        elif event_type == "update_ball":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "update_ball",
                    "ball_x": data["ball_x"],
                    "ball_y": data["ball_y"],
                }
            )
        elif event_type == "sound_play":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "sound_play",
                    "sound": data["sound"],
                }
            )
        elif event_type == "game_over":
            match = await self.update_match_winner(data["winner_id"], data["score_user1"], data["score_user2"])
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "game_finished",
                    "winner": match.winner.username if match.winner else None,
                    "score_user1": match.score_user1,
                    "score_user2": match.score_user2,
                }
            )

    async def update_paddle(self, event):
        await self.send(text_data=json.dumps(event))

    async def update_score(self, event):
        await self.send(text_data=json.dumps(event))

    async def update_ball(self, event):
        await self.send(text_data=json.dumps(event))

    async def game_finished(self, event):
        await self.send(text_data=json.dumps(event))

    async def update_match_winner(self, winner_id, score1, score2):
        match = await Match.objects.aget(id=self.match_id)
        winner = await User.objects.aget(id=winner_id)
        match.winner = winner
        match.score_user1 = score1
        match.score_user2 = score2
        match.finished_date_played = now()
        await match.asave()
        return match
