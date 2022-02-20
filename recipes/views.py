from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class RecipesView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "recipes/recipes.html")


class AddRecipeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "recipes/add_recipe.html")
