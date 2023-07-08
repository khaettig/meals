from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory

from recipes.models import Recipe

from .category_factory import CategoryFactory


class RecipeFactory(DjangoModelFactory):
    class Meta:
        model = Recipe

    name = Sequence(lambda n: f"Recipe {n}")
    category = SubFactory(CategoryFactory)
