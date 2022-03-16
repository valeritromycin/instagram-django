from django.shortcuts import render, redirect
from django.views.generic import ListView

from registration_app.forms import RegistrationForm
from .models import Post


def main_page(request):
    posts = Post.objects.order_by('-create_date').all()
    context = {'title': 'insta-django', 'posts': posts}
    return render(request, 'main_page.html', context)


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main_page.html'
    context_object_name = 'posts'
    ordering = ("-create_date", "-id")
    http_method_names = ['get', ]
    form_class = RegistrationForm

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.all()
        return self.queryset.filter(is_public=True).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = "Posts"
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        return result


