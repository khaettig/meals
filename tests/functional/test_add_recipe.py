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

        add_recipe_page.submit.click()
        self.assert_page_active(AddRecipePage)
        self.assert_page_has_html5_invalid_field()

        add_recipe_page.name.send_keys("Macaroni and Cheese")
        add_recipe_page.description.send_keys("Boil the pasta, drain. Add cheese.")
        add_recipe_page.submit.click()
        self.assert_page_active(AddRecipePage)
        self.assertIn("Your recipe was saved!", add_recipe_page.body.text)

        add_recipe_page.link("Recipes").click()
        self.assertEqual("Recipes", recipes_page.title)
        self.assertIn("Macaroni and Cheese", recipes_page.body.text)
