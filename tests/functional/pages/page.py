from selenium.webdriver.common.by import By


class Page:
    def __init__(self, browser, live_server_url):
        self.browser = browser
        self.live_server_url = live_server_url

    def open(self, **kwargs):
        self.browser.get(self.live_server_url + self.url.format(**kwargs))

    @property
    def title(self):
        return self.browser.title

    @property
    def body(self):
        return self.browser.find_element(By.TAG_NAME, "body")

    def link(self, text):
        return self.browser.find_element(By.LINK_TEXT, text)
