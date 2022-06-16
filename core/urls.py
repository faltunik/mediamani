from django.urls import path
from . import views


urlpatterns = [
    path('audiospeed', views.audio_speed, name='audio_speed'),
    path('audioextracter', views.audio_extracter, name='audio_extract'),
]