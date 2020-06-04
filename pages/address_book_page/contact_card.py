from selenium.common.exceptions import TimeoutException

from framework.page import BasePage
from selenium.webdriver.common.by import By


class ContactCard(BasePage):
    class Locators:
        REMOVE_BUTTON = (By.XPATH, '//div[@data-name="remove"]')
        CONFIRM_BUTTONS_ARRAY = (By.XPATH, '//*[contains(@class, \'btn btn_main confirm-ok\')]')

        FIRST_PHONE_EDIT_FORM = (By.ID, 'phones_0')

        PHONES_ARRAY = (By.XPATH, '//span[@class="contact__phones__item__value"]')
        EMAILS_ARRAY = (By.XPATH, '//a[@class="js-email-address"]')
        JOB_TITLE_ARRAY = (By.XPATH, '//span[@class="contact__job__item contact__job__item_job_title"]')
        BOSS_ARRAY = (By.XPATH, '//div[@class="contact__job__item contact__job__item_boss"]')
        NICK_ARRAY = (By.XPATH, '//span[@class="contact__header__title__additional"]')
        GENDER_HEADER = (By.XPATH, '//div[@class="contact__header__additional"]')

        @staticmethod
        def current_contact_container_in_card(lastname: str, new_firstname: str):
            if not new_firstname:
                return By.XPATH, f'//*[text()=\'{lastname}\']'
            if not lastname:
                return By.XPATH, f'//*[text()=\'{new_firstname}\']'
            return By.XPATH, f'//*[text()=\'{lastname} {new_firstname}\']'

    def check_contact_title_by_firstname_and_lastname(self, new_firstname, lastname):
        try:
            self.wait_for_visible(*self.Locators.current_contact_container_in_card(lastname, new_firstname))
            return True
        except TimeoutException:
            return False

    def click_remove_button(self):
        self.wait_for_clickable(*self.Locators.REMOVE_BUTTON).click()

    def confirm_remove(self):
        buttons_in_list = self.wait_for_all_elements(*self.Locators.CONFIRM_BUTTONS_ARRAY)
        buttons_in_list[0].click()

    def phone_was_added_successfully(self, new_phone):
        contact_phones = self.wait_for_all_elements(*self.Locators.PHONES_ARRAY)
        return contact_phones[-1].text == new_phone

    def email_was_added_successfully(self, new_email):
        contact_emails = self.wait_for_all_elements(*self.Locators.EMAILS_ARRAY)
        return contact_emails[-1].text == new_email

    def job_title_was_added_successfully(self, job_title):
        value_in_contact_card = self.wait_for_all_elements(*self.Locators.JOB_TITLE_ARRAY)
        return value_in_contact_card[-1].text == job_title

    def boss_was_added_successfully(self, boss):
        value_in_contact_card = self.wait_for_all_elements(*self.Locators.BOSS_ARRAY)
        return value_in_contact_card[-1].text.split()[1] == boss

    def nick_was_added_successfully(self, nick):
        check_value = f'«{nick}»'
        value_in_contact_card = self.wait_for_all_elements(*self.Locators.NICK_ARRAY)
        return value_in_contact_card[-1].text == check_value

    def gender_was_added_successfully(self):
        contact_header = self.wait_for_visible(*self.Locators.GENDER_HEADER)
        return contact_header.text == 'Мужской'

    def job_title_was_deleted(self):
        job_title_element = self.driver.find_elements(*self.Locators.JOB_TITLE_ARRAY)
        if not job_title_element:
            return True
        return False

    def nick_was_deleted(self):
        nick_element = self.driver.find_elements(*self.Locators.NICK_ARRAY)
        if not nick_element:
            return True
        return False

    def boss_was_deleted(self):
        boss_element = self.driver.find_elements(*self.Locators.BOSS_ARRAY)
        if not boss_element:
            return True
        return False
