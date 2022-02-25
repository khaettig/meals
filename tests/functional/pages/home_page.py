from selenium.webdriver.common.by import By

from .page import Page


class HomePage(Page):
    url = "/"

    @property
    def logout(self):
        return self.browser.find_element(By.ID, "logout")
