from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('upload_audio', views.upload_audio, name='upload_audio'),
    path('out_audio', views.out_audio, name='out_audio'),
    path('tts', views.tts, name='tts'),
    path('test', views.test, name='test'),
    path('test2', views.test2, name='test2')
]
