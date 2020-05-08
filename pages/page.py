class Page(object):
    def __init__(self, url, driver):
        self.base_url = url
        self.driver = driver

    def open(self):
        self.driver.get(self.base_url)
