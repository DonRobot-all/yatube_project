from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .models import Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Проверка title в index из контекста'
    context = {
        'posts': posts,
        'title': title,
        'text': 'Информация на главной странице из контекста'
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
