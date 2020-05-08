# coding=utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .page import Page


class AddressBookPage(Page):
    def click_xpath(self, xpath):
        return self.wait_for_visible_xpath(xpath).click()

    def wait_for_visible_xpath(self, xpath):
        return WebDriverWait(self.driver, 32).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def test_edit_contact(self):
        self.click_xpath('//input[@class="messageline__checkbox__input"]')
        self.click_xpath('//div[@data-name="edit"]')
        self.wait_for_visible_xpath('//form[@id="formPersonal"]')
