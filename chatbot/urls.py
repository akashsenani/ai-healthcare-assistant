from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.chatbot_view,
        name='chatbot'
    ),

    path(
    'voice-ai/',
    views.voice_ai,
    name='voice_ai'
    ),  
]
