from django.utils.timezone import now


def update_recipe(*, recipe, name, description, url, actor):
    recipe.name = name
    recipe.description = description
    recipe.url = url
    recipe.updated_at = now()
    recipe.save()
