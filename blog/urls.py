"""Создали urls уровня приложения"""
from django.urls import path

from blog.views import post_list, post_detail

app_name = 'blog'  # Пространство имен приложения, должно быть уникальным по всему проекту

urlpatterns = [
    path('<int:year>/<int:month>/<int: day>/<slug: post>/', post_detail, name='post_detail'),
    path('', post_list, name='post_list'),  # name позволит нам обращаться к этому представлению из любой точки проекта
    # по имени (app_name : name)  в нашем случае ***  urls "blog:post_list"  ***
]
