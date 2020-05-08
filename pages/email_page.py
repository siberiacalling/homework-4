from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .page import Page


class EmailPage(Page):
    def switch_to_address_book(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"/addressbook")]')))
        element.click()
