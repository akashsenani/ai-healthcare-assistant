from django.shortcuts import render
import markdown
from django.http import JsonResponse

from .gemini_chatbot import (
    medical_chatbot,
    voice_medical_chatbot
)

from users.models import ChatbotHistory

import json

# =====================================================
# CHATBOT PAGE
# =====================================================

def chatbot_view(request):

    # FETCH OLD CHATS
    chats = []

    if request.user.is_authenticated:

        chats = ChatbotHistory.objects.filter(

            user=request.user

        ).order_by('created_at')

    # NEW MESSAGE
    if request.method == 'POST':

        user_message = request.POST['message']

        raw_response = medical_chatbot(
            user_message
        )

        response = markdown.markdown(
            raw_response
        )

        # SAVE CHAT
        if request.user.is_authenticated:

            ChatbotHistory.objects.create(

                user=request.user,

                question=user_message,

                response=response
            )

        # REFRESH CHAT HISTORY
        chats = ChatbotHistory.objects.filter(

            user=request.user

        ).order_by('created_at')

    return render(

        request,

        'chatbot.html',

        {

            'chats': chats
        }
    )

# =====================================================
# VOICE AI
# =====================================================

def voice_ai(request):

    if request.method == 'POST':

        data = json.loads(
            request.body
        )

        user_message = data.get(
            'message'
        )

        response = voice_medical_chatbot(
        user_message
        )

        return JsonResponse({

            'response': response
        })

    return render(

        request,

        'voice_assistant.html'
    )