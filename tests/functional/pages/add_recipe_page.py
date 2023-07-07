from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .page import Page


class AddRecipePage(Page):
    url = "/recipes/add/"

    @property
    def name(self):
        return self.browser.find_element(By.ID, "id_name")

    @property
    def description(self):
        return self.browser.find_element(By.ID, "id_description")

    @property
    def category(self):
        return Select(self.browser.find_element(By.ID, "id_category_id"))

    @property
    def submit(self):
        return self.browser.find_element(By.ID, "submit_recipe")
