from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')
# Страница со списком групп
def posts_groups_list(request):
    return HttpResponse('Список групп')
# Страница с конкретной группой
def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')