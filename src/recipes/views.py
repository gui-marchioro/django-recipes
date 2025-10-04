from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: HttpRequest, category_id: int) -> HttpResponse:
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    return render(request, "recipes/pages/recipe-view.html", context={
        "recipe": make_recipe(),
        "is_detail_page": True,
    })
