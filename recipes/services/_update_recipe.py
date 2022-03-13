from django.utils.timezone import now

from recipes.models import Recipe

from ._exceptions import RecipeAlreadyExists


def update_recipe(*, recipe, name, description, url, actor):
    if Recipe.objects.exclude(id=recipe.id).filter(name=name).exists():
        raise RecipeAlreadyExists

    recipe.name = name
    recipe.description = description
    recipe.url = url
    recipe.updated_at = now()
    recipe.save()
