from factory import Sequence
from factory.django import DjangoModelFactory

from recipes.models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = Sequence(lambda n: f"Category {n}")
