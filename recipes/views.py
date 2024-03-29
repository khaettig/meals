from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from core.utils import get_fields, get_ordering_field
from recipes import messages
from recipes.forms import RecipeForm
from recipes.models import Recipe
from recipes.services import create_recipe, update_recipe


class RecipesView(LoginRequiredMixin, View):
    def get(self, request):
        filter = request.GET.get("filter", "").lower()
        ordering = request.GET.get("ordering", "name")
        ordering_field = get_ordering_field(
            key=ordering,
            options={
                "name": "name",
                "category": "category__name",
                "creator": "creator__first_name",
            },
        )

        recipes = (
            Recipe.objects.select_related("creator", "category")
            .filter(
                Q(name__icontains=filter)
                | Q(creator__username__icontains=filter)
                | Q(category__name__icontains=filter)
            )
            .order_by(ordering_field)
        )

        return render(
            request,
            "recipes/recipes_table.html" if request.htmx else "recipes/recipes.html",
            context={
                "recipes": recipes,
                "ordering": ordering,
            },
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
            with form.handles_specified_exceptions():
                create_recipe(**form.cleaned_data, actor=request.user)
                messages.add_recipe_created_message(request)
                return redirect("recipes:add_recipe")
        return self._render(request, form=form)

    def _render(self, request, *, form):
        return render(request, "recipes/add_recipe.html", context={"form": form})


class EditRecipeView(LoginRequiredMixin, View):
    def dispatch(self, request, recipe_id):
        self.recipe = get_object_or_404(Recipe, id=recipe_id)
        return super().dispatch(request)

    def get(self, request):
        return self._render(request, form=RecipeForm(initial=get_fields(self.recipe)))

    def post(self, request):
        form = RecipeForm(request.POST)

        if form.is_valid():
            with form.handles_specified_exceptions():
                update_recipe(
                    recipe=self.recipe, **form.cleaned_data, actor=request.user
                )
                messages.add_recipe_saved_message(request)
                return redirect("recipes:edit_recipe", recipe_id=self.recipe.id)
        return self._render(request, form=form)

    def _render(self, request, *, form):
        return render(
            request,
            "recipes/edit_recipe.html",
            context={"form": form, "recipe": self.recipe},
        )
