from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.disease_prediction,
        name='prediction'
    ),
]