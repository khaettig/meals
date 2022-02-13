from selenium.webdriver.common.keys import Keys

from core.factories import UserFactory

from .pages import HomePage, LoginPage
from .utils import FunctionalTest


class AuthenticationTest(FunctionalTest):
    def test_login_and_logout(self):
        UserFactory(username="testuser", password="correctpassword")

        home_page = self.get_page(HomePage)
        login_page = self.get_page(LoginPage)

        # Unauthenticated user gets redirected to login page
        home_page.open()
        self.assert_page_active(LoginPage)

        # Wrong password doesn't log in user
        login_page.username.send_keys("testuser")
        login_page.password.send_keys("wrongpassword")
        login_page.password.send_keys(Keys.ENTER)
        self.assert_page_active(LoginPage)

        # Correct password does log in user
        login_page.password.send_keys("correctpassword")
        login_page.password.send_keys(Keys.ENTER)
        self.assert_page_active(HomePage)

        # User can see his/her name in the header
        self.assertEqual(home_page.logged_in_as.text, "Logged in as testuser")

        # User can log out and is redirected to login page
        home_page.logout.click()
        self.assert_page_active(LoginPage)
