"""Создали urls уровня приложения"""
from django.urls import path

from blog import views

app_name = 'blog'  # Имя уровня приложения, должно быть уникальным по всему проекту

urlpatterns = [
    path('', views.index, name='home'),
]
