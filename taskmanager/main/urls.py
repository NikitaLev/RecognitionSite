from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('upload_audio', views.upload_audio, name='upload_audio'),
    path('out_audio', views.out_audio, name='out_audio')
]
