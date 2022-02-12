from selenium.webdriver.common.by import By

from .page import Page


class LoginPage(Page):
    url = "/login/"

    @property
    def username(self):
        return self.browser.find_element(By.ID, "id_username")

    @property
    def password(self):
        return self.browser.find_element(By.ID, "id_password")
