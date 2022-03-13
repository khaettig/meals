from selenium.webdriver.common.by import By

from .page import Page


class EditRecipePage(Page):
    url = "/recipes/edit/{recipe_id}/"

    @property
    def name(self):
        return self.browser.find_element(By.ID, "id_name")

    @property
    def description(self):
        return self.browser.find_element(By.ID, "id_description")

    @property
    def url_(self):
        return self.browser.find_element(By.ID, "id_url")

    @property
    def submit(self):
        return self.browser.find_element(By.ID, "submit_recipe")

    @property
    def back(self):
        return self.browser.find_element(By.LINK_TEXT, "Back")
