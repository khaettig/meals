from selenium.webdriver.common.by import By

from .page import Page


class RecipesPage(Page):
    url = "/recipes/"

    @property
    def add_recipe(self):
        return self.browser.find_element(By.ID, "add_recipe")
