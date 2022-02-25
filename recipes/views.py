from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View

from recipes.forms import AddRecipeForm


class RecipesView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "recipes/recipes.html")


class AddRecipeView(LoginRequiredMixin, View):
    def get(self, request):
        return self._render(request, form=AddRecipeForm())

    def post(self, request):
        form = AddRecipeForm(request.POST)

        if form.is_valid():
            messages.add_message(
                request, messages.INFO, "Your recipe was saved!", extra_tags="success"
            )
            return redirect("recipes:add_recipe")
        return self._render(request, form=form)

    def _render(self, request, *, form):
        return render(request, "recipes/add_recipe.html", context={"form": form})
