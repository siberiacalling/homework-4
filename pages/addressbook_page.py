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

    def edit_contact_without_selected_contact(self):
        old_window_url = self.driver.current_url
        self.click_xpath('//div[@data-name="edit"]')
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def edit_contact_two_selected_contact(self):
        old_window_url = self.driver.current_url
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[2]')
        self.click_xpath('//div[@data-name="edit"]')

        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def edit_contact(self):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')
        self.wait_for_visible_xpath('//form[@id="formPersonal"]')