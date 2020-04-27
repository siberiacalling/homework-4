from framework.page import Page


class Steps(object):
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url):
        self.page.driver.get(url)

    def open(self):
        pass
