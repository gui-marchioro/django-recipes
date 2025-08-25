from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "recipes/home.html")


def contato(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Contato")


def sobre(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Sobre")
