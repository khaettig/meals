from django.test import TestCase

from core.factories import UserFactory
from recipes.models import Recipe
from recipes.services import create_recipe


class AddRecipeTest(TestCase):
    def test_with_minimal_information(self):
        actor = UserFactory()

        create_recipe(name="Pizza", actor=actor)

        recipe = Recipe.objects.get()
        self.assertEqual(recipe.name, "Pizza")

    def test_with_maximal_information(self):
        actor = UserFactory()

        create_recipe(
            name="Sushi",
            description="Order it.",
            url="sushi.com",
            actor=actor,
        )

        recipe = Recipe.objects.get()
        self.assertEqual(recipe.name, "Sushi")
        self.assertEqual(recipe.description, "Order it.")
        self.assertEqual(recipe.url, "sushi.com")
        self.assertEqual(recipe.creator, actor)
