from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from recipes.forms import AddRecipeForm
from recipes.models import Recipe
from recipes.services import create_recipe


class RecipesView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            "recipes/recipes.html",
            context={"recipes": Recipe.objects.all()},
        )


class RecipeView(LoginRequiredMixin, View):
    def get(self, request, recipe_id):
        return render(
            request,
            "recipes/recipe.html",
            context={"recipe": get_object_or_404(Recipe, id=recipe_id)},
        )


class AddRecipeView(LoginRequiredMixin, View):
    def get(self, request):
        return self._render(request, form=AddRecipeForm())

    def post(self, request):
        form = AddRecipeForm(request.POST)

        if form.is_valid():
            create_recipe(**form.cleaned_data, actor=request.user)
            messages.add_message(
                request, messages.INFO, "Your recipe was saved!", extra_tags="success"
            )
            return redirect("recipes:add_recipe")
        return self._render(request, form=form)

    def _render(self, request, *, form):
        return render(request, "recipes/add_recipe.html", context={"form": form})
