from django.urls import re_path
from . import consumers

websocket_urlptterns = [
    re_path(r'room/(?P<group>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]
