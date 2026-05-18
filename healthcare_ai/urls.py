from django.contrib import admin

from django.urls import (
    path,
    include
)

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    # USERS
    path(
        '',
        include('users.urls')
    ),

    # PREDICTION
    path(
        'prediction/',
        include('prediction.urls')
    ),

    # CHATBOT
    path(
        'chatbot/',
        include('chatbot.urls')
    ),

    # DASHBOARD
    path(
        'dashboard/',
        include('dashboard.urls')
    ),
]