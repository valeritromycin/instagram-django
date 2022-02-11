from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from registration_app.forms.registrations import RegistrationForm
from registration_app.forms.auth import Authorisation


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


def authorisation_page(request):
    error = False
    if request.method == "POST":
        form = Authorisation(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next', '/')
                return redirect(next_page)
            error = True
    else:
        form = Authorisation()
    context = {
        'authorisation_page': Authorisation, 'error': error
    }
    return render(request, "authorisation_page.html", context)
