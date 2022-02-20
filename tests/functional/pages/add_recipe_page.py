from selenium.webdriver.common.by import By

from .page import Page


class AddRecipePage(Page):
    url = "/recipes/add_recipe/"

    @property
    def name(self):
        return self.browser.find_element(By.ID, "id_name")

    @property
    def description(self):
        return self.browser.find_element(By.ID, "id_description")

    @property
    def submit(self):
        return self.browser.find_element(By.ID, "submit_recipe")
