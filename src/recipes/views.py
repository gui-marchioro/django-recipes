from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home")


def contato(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Contato")


def sobre(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Sobre")
