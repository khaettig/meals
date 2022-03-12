from selenium.webdriver.common.by import By

from tests.functional.utils.table import get_table_fields

from .page import Page


class RecipesPage(Page):
    url = "/recipes/"

    @property
    def add_recipe(self):
        return self.browser.find_element(By.ID, "add_recipe")

    @property
    def recipes(self):
        return [
            get_table_fields(recipe, {"name": ".name", "name__url": ".name a"})
            for recipe in self.browser.find_elements(By.CLASS_NAME, "recipe")
        ]
