from recipes.models import Recipe


def create_recipe(*, name, description=None, url=None, actor):
    Recipe.objects.create(name=name, description=description, url=url, creator=actor)
