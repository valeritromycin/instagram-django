from django.shortcuts import render, redirect

from .forms.registrations import RegistrationForm
from .models import Post


def main_page(request):
    posts = Post.objects.order_by('-create_date').all()
    context = {'title': 'Hello world', 'posts': posts}
    return render(request, 'main_page.html', context)


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
    context = {
        'registration_page': RegistrationForm
    }
    return render(request, "registration_page.html", context)
