from selenium.webdriver.common.keys import Keys

from .pages import LoginPage
from .utils import FunctionalTest


class AuthenticationTest(FunctionalTest):
    def test_login_and_logout(self):
        login_page = self.get_page(LoginPage)
        login_page.open()
        self.assertEqual("Login", login_page.title)

        login_page.username.send_keys("testuser")
        login_page.password.send_keys("wrongpassword")
        login_page.password.send_keys(Keys.ENTER)

        self.assertEqual("Login", login_page.title)

        login_page.username.send_keys("testuser")
        login_page.password.send_keys("correctpassword")
        login_page.password.send_keys(Keys.ENTER)
