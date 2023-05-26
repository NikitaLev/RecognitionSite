from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('out_audio', views.out_audio, name='out_audio'),
    path('stt', views.stt, name='stt'),
    path('see', views.see, name='see'),
    path('tts', views.tts, name='tts'),
    path('test', views.test, name='test'),
    path('test2', views.test2, name='test2')
]
