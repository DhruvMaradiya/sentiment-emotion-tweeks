"""sentiment_emotion_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
    """


from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentiment/', include('sentiment.urls')),
    path('', include('sentiment_or_emotion.urls')),
    path('emotion/', include('emotion.urls')),
]
