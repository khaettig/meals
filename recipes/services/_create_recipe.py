from recipes.models import Category, Recipe

from ._exceptions import RecipeAlreadyExists


def create_recipe(*, name, description=None, category_id=0, url=None, actor):
    if Recipe.objects.filter(name=name).exists():
        raise RecipeAlreadyExists

    category = Category.objects.get(id=category_id)

    return Recipe.objects.create(
        name=name, description=description, category=category, url=url, creator=actor
    )
