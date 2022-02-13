from decouple import config
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from .http import remove_get_parameters


class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        super().setUp()

        chrome_options = Options()

        if not config("SHOW", default=False, cast=bool):
            chrome_options.add_argument("--headless")

        self.browser = Chrome(options=chrome_options)

    def tearDown(self):
        super().tearDown()

        self.browser.quit()

    @property
    def current_url(self):
        assert self.browser.current_url.startswith(self.live_server_url)
        return self.browser.current_url.replace(self.live_server_url, "")

    def get_page(self, Class):
        return Class(self.browser, self.live_server_url)

    def assert_page_active(self, Class):
        return self.assertEqual(remove_get_parameters(self.current_url), Class.url)
