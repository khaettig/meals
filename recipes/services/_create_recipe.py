from recipes.models import Recipe

from ._exceptions import RecipeAlreadyExists


def create_recipe(*, name, description=None, url=None, actor):
    if Recipe.objects.filter(name=name).exists():
        raise RecipeAlreadyExists

    return Recipe.objects.create(
        name=name, description=description, url=url, creator=actor
    )
