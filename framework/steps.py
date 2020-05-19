from framework.page import BasePage


class BaseSteps(object):
    page: BasePage

    def __init__(self, page: BasePage):
        self.page = page

    def open_url(self, url):
        self.page.driver.get(url)

    def open(self):
        pass
