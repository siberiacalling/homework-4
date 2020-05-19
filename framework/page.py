from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    __timeout = 10
    __frequency = 0.1

    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_for_visible(self, by, value) -> WebElement:
        return self.__wait().until(EC.presence_of_element_located((by, value)))

    def wait_for_invisible(self, by, value):
        self.__wait().until(EC.invisibility_of_element_located((by, value)))

    def wait_for_clickable(self, by, value) -> WebElement:
        return self.__wait().until(EC.element_to_be_clickable((by, value)))

    def wait_for_url(self, url: str):
        self.__wait().until(lambda driver: driver.current_url == url)

    def __wait(self) -> WebDriverWait:
        return WebDriverWait(self.driver, self.__timeout, self.__frequency)
