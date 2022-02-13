from selenium.webdriver.common.by import By

from .page import Page


class HomePage(Page):
    url = "/"

    @property
    def logged_in_as(self):
        return self.browser.find_element(By.ID, "logged_in_as")

    @property
    def logout(self):
        return self.browser.find_element(By.ID, "logout")
