from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from recipes.forms import RecipeForm
from recipes.models import Recipe
from recipes.services import create_recipe, update_recipe


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
        return self._render(request, form=RecipeForm())

    def post(self, request):
        form = RecipeForm(request.POST)

        if form.is_valid():
            create_recipe(**form.cleaned_data, actor=request.user)
            messages.add_message(
                request, messages.INFO, "Your recipe was saved!", extra_tags="success"
            )
            return redirect("recipes:add_recipe")
        return self._render(request, form=form)

    def _render(self, request, *, form):
        return render(request, "recipes/add_recipe.html", context={"form": form})


class EditRecipeView(LoginRequiredMixin, View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        return self._render(
            request,
            form=RecipeForm(
                initial={
                    "name": recipe.name,
                    "description": recipe.description,
                    "url": recipe.url,
                }
            ),
            recipe=recipe,
        )

    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(request.POST)

        if form.is_valid():
            update_recipe(recipe=recipe, **form.cleaned_data, actor=request.user)
            messages.add_message(
                request, messages.INFO, "Your recipe was saved!", extra_tags="success"
            )
            return redirect("recipes:edit_recipe", recipe_id=recipe_id)
        return self._render(request, form=form, recipe=recipe)

    def _render(self, request, *, form, recipe):
        return render(
            request,
            "recipes/edit_recipe.html",
            context={"form": form, "recipe": recipe},
        )
