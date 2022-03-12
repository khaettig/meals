from .pages import AddRecipePage, HomePage, RecipePage, RecipesPage
from .utils import FunctionalTest

RECIPE_NAME = "Macaroni and Cheese"
RECIPE_DESCRIPTION = "Boil the pasta, drain. Add cheese."


class AddRecipeTest(FunctionalTest):
    def test_add_recipe(self):
        self.login()

        home_page = self.get_page(HomePage)
        recipes_page = self.get_page(RecipesPage)
        add_recipe_page = self.get_page(AddRecipePage)
        recipe_page = self.get_page(RecipePage)

        home_page.open()
        home_page.link("Recipes").click()
        self.assertEqual("Recipes", recipes_page.title)

        recipes_page.add_recipe.click()
        self.assert_page_active(AddRecipePage)

        add_recipe_page.submit.click()
        self.assert_page_active(AddRecipePage)
        self.assert_page_has_html5_invalid_field()

        add_recipe_page.name.send_keys(RECIPE_NAME)
        add_recipe_page.description.send_keys(RECIPE_DESCRIPTION)
        add_recipe_page.submit.click()
        self.assert_page_active(AddRecipePage)
        self.assertIn("Your recipe was saved!", add_recipe_page.body.text)

        add_recipe_page.link("Recipes").click()
        self.assertEqual("Recipes", recipes_page.title)
        recipe = recipes_page.recipes[0]
        self.assertEqual(recipe["name"].text, RECIPE_NAME)

        recipe["name__url"].click()
        self.assert_page_active(RecipePage, recipe_id=recipe["id"])

        self.assertEqual(RECIPE_NAME, recipe_page.title)
        self.assertEqual(RECIPE_NAME, recipe_page.content_title.text)
        self.assertEqual(RECIPE_DESCRIPTION, recipe_page.description.text)
