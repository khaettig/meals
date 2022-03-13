from selenium.webdriver.common.by import By

from .page import Page


class RecipePage(Page):
    url = "/recipes/{recipe_id}/"

    @property
    def content_title(self):
        return self.browser.find_element(By.TAG_NAME, "h3")

    @property
    def description(self):
        return self.browser.find_element(By.CLASS_NAME, "description")

    @property
    def edit(self):
        return self.browser.find_element(By.LINK_TEXT, "Edit")
