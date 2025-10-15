from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: HttpRequest, category_id: int) -> HttpResponse:
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by('-id')
    recipe = recipes.first()
    if not recipe:
        raise Http404('Category not found')
    category = recipe.category
    if not category:
        raise Http404('Category not found')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{category.name} - Category |',
    })


def recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    return render(request, "recipes/pages/recipe-view.html", context={
        "recipe": make_recipe(),
        "is_detail_page": True,
    })
