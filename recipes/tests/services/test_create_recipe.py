from django.test import TestCase

from core.factories import UserFactory
from recipes.models import Recipe
from recipes.services import RecipeAlreadyExists, create_recipe


class AddRecipeTest(TestCase):
    fixtures = ["fixtures/category.yaml"]

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
            category_id=3,
            url="sushi.com",
            actor=actor,
        )

        recipe = Recipe.objects.get()
        self.assertEqual(recipe.name, "Sushi")
        self.assertEqual(recipe.description, "Order it.")
        self.assertEqual(recipe.category.name, "Pasta")
        self.assertEqual(recipe.url, "sushi.com")
        self.assertEqual(recipe.creator, actor)

    def test_creating_recipe_with_same_name_raises_already_exists(self):
        actor = UserFactory()
        create_recipe(name="Pizza", actor=actor)

        with self.assertRaises(RecipeAlreadyExists):
            create_recipe(name="Pizza", actor=actor)
