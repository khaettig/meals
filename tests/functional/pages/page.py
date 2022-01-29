class Page:
    def __init__(self, browser, live_server_url):
        self.browser = browser
        self.live_server_url = live_server_url

    def open(self):
        self.browser.get(self.live_server_url + self.url)

    @property
    def title(self):
        return self.browser.title
