from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {'title': title,}
    return render(request, template, context)


def posts_groups_list(request):
    template = 'posts/posts_list'
    return render(request, template)


def group_posts(request, slug):
    #group = get_object_or_404(group, slug=slug)
    template = 'posts/group_list.html'
    title = '"Здесь будет информация о группах проекта Yatube"'
    posts = Post.object.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts}
    return render(request, template, context)