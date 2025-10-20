from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from .models import Recipe


def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: HttpRequest, category_id: int) -> HttpResponse:
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))
    category = recipes[0].category
    if not category:
        raise Http404('Category not found')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{category.name} - Category |',
    })


def recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    recipe = get_object_or_404(Recipe, pk=recipe_id, is_published=True)
    return render(request, "recipes/pages/recipe-view.html", context={
        "recipe": recipe,
        "is_detail_page": True,
    })


def search(request: HttpRequest) -> HttpResponse:
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes,
    })
