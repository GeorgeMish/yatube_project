# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком групп
    path('group/', views.posts_groups_list),
    # Страница с постами одной группы
    path('group/<slug:slug>', views.group_posts),
]