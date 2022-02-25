from decouple import config
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from core.factories import UserFactory

from ..pages import LoginPage
from .http import remove_get_parameters


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()

        chrome_options = Options()

        if not config("SHOW", default=False, cast=bool):
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080")

        self.browser = Chrome(options=chrome_options)

    def tearDown(self):
        super().tearDown()

        self.browser.quit()

    def login(self):
        UserFactory(username="testuser", password="correctpassword")

        login_page = self.get_page(LoginPage)
        login_page.open()
        login_page.username.send_keys("testuser")
        login_page.password.send_keys("correctpassword")
        login_page.password.send_keys(Keys.ENTER)

    @property
    def current_url(self):
        assert self.browser.current_url.startswith(self.live_server_url)
        return self.browser.current_url.replace(self.live_server_url, "")

    def get_page(self, Class):
        return Class(self.browser, self.live_server_url)

    def assert_page_active(self, Class):
        return self.assertEqual(remove_get_parameters(self.current_url), Class.url)

    def assert_page_has_html5_invalid_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, ":required, :invalid")
