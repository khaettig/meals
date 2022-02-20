from .pages import AddRecipePage, HomePage, RecipesPage
from .utils import FunctionalTest


class AddRecipeTest(FunctionalTest):
    def test_add_recipe(self):
        self.login()

        home_page = self.get_page(HomePage)
        recipes_page = self.get_page(RecipesPage)
        add_recipe_page = self.get_page(AddRecipePage)

        home_page.open()
        home_page.link("Recipes").click()
        self.assertEqual("Recipes", recipes_page.title)

        recipes_page.add_recipe.click()
        self.assert_page_active(AddRecipePage)
