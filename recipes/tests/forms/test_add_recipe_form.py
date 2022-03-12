from django.test import TestCase

from recipes.forms import AddRecipeForm
from recipes.services import create_recipe


class AddRecipeFormTest(TestCase):
    def test_ensures_names_are_unique(self):
        create_recipe(name="existing recipe", actor=None)
        form = AddRecipeForm(data={"name": "existing recipe"})

        form.is_valid()

        self.assertIn("name", form.errors)
