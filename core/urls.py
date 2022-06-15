from django.urls import path
from . import views


urlpatterns = [
    path('audiospeed', views.audio_speed, name='index'),
]