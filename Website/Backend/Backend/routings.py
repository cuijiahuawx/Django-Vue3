from django.urls import re_path, path, include
from channels.routing import URLRouter
import chat.routings as chat_routings

websocket_urlptterns = [
    path('chat/', URLRouter(chat_routings.websocket_urlptterns), name='chat'),
]

