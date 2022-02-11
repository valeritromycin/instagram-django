from django.shortcuts import render, redirect
from .models import Post


def main_page(request):
    posts = Post.objects.order_by('-create_date').all()
    context = {'title': 'Hello world', 'posts': posts}
    return render(request, 'main_page.html', context)

