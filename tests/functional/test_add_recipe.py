from .pages import AddRecipePage
from .utils import FunctionalTest


class AddRecipeTest(FunctionalTest):
    def test_add_recipe(self):
        add_recipe_page = self.get_page(AddRecipePage)
        add_recipe_page.open()

        self.assertEqual("Add a recipe", add_recipe_page.title)
