from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from .forms import RegisterForm


def register_view(request: HttpRequest) -> HttpResponse:
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register.html', {
        'form': form,
    })


def registered_view(request: HttpRequest) -> HttpResponse:
    if not request.POST:
        raise Http404()

    request.session["register_form_data"] = request.POST
    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Your user is created, please log in.')

        del (request.session['register_form_data'])

    return redirect("authors:register")
