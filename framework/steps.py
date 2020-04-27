from framework.page import Page


class Steps(object):
    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.driver.get(url)
