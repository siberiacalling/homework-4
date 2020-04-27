from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver import Remote


class Page(object):
    __timeout = 10
    __frequency = 0.1

    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_for_visible_by_selector(self, selector: str):
        self.__wait().until(expect.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_for_visible_by_xpath(self, xpath: str):
        self.__wait().until(expect.visibility_of_element_located((By.XPATH, xpath)))

    def wait_for_url(self, url: str):
        self.__wait().until(lambda driver: driver.current_url == url)

    def __wait(self) -> WebDriverWait:
        return WebDriverWait(self.driver, self.__timeout, self.__frequency)
