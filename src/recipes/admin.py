from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):  # type: ignore
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):  # type: ignore
    ...


admin.site.register(Category, CategoryAdmin)  # type: ignore
