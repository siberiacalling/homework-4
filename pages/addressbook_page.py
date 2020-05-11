# coding=utf-8
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .page import Page


class AddressBookPage(Page):
    def click_xpath(self, xpath):
        return self.wait_for_visible_xpath(xpath).click()

    def wait_for_visible_xpath(self, xpath):
        return WebDriverWait(self.driver, 32).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def fill_contact(self, firstname, lastname, company, email, phone):
        element = self.driver.find_element_by_name("firstname")
        element.send_keys(firstname)

        element = self.driver.find_element_by_name("lastname")
        element.send_keys(lastname)

        element = self.driver.find_element_by_name("company")
        element.send_keys(company)

        element = self.driver.find_element_by_name("emails")
        element.send_keys(email)

        element = self.driver.find_element_by_id("phones_0")
        element.send_keys(phone)

        self.click_xpath('//div[@data-name="submit"]')

    def create_test_contact(self, firstname, lastname, company, email, phone):
        self.click_xpath('//div[@data-name="add"]')
        self.fill_contact(firstname, lastname, company, email, phone)

    def click_contact_in_list(self, firstname, lastname):
        search_string = lastname + " " + firstname
        xpath = '//span[text()=\'' + search_string + '\']'
        child_element = self.driver.find_elements_by_xpath(xpath)
        parent_element = child_element[0].find_element_by_xpath('..')
        parent_element2 = parent_element.find_element_by_xpath('..')
        parent_element2.click()

    def delete_tested_contact(self, firstname, lastname):
        # self.click_contact_in_list(firstname, lastname)
        self.click_xpath('//div[@data-name="remove"]')
        confirm_button = self.driver.find_elements_by_xpath('//*[contains(@class, \'btn btn_main confirm-ok\')]')
        confirm_button[0].click()

    def change_email_field(self, new_email):
        element = self.driver.find_element_by_name("emails")
        element.click()
        element.clear()
        element.send_keys(new_email)
        self.click_xpath('//div[@data-name="submit"]')

    def random_with_n_digits(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    def change_firstname_field(self, firstname, lastname, new_firstname, from_list=False):
        if from_list:
            self.click_contact_in_list(firstname, lastname)

        self.click_xpath('//div[@data-name="edit"]')
        element = self.driver.find_element_by_name("firstname")
        element.click()
        element.clear()
        element.send_keys(new_firstname)
        self.click_xpath('//div[@data-name="submit"]')

    def click_contact_checkbox(self):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[-1]')

    def check_edited_field(self, new_firstname, lastname):
        search_string = lastname + " " + new_firstname
        xpath = '//*[contains(text(), \'' + search_string + '\')]'

        child_element = self.driver.find_elements_by_xpath(xpath)
        if child_element:
            return True
        return False

    def go_to_contact_list(self):
        self.click_xpath('//span[text()=\'Все контакты\']')

    def change_email(self, new_email):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')
        old_window_url = self.driver.current_url
        self.change_email_field(new_email)
        new_window_url = self.driver.current_url
        return old_window_url == new_window_url

    # tests
    def test_edit_contact_without_selected_contact(self):
        old_window_url = self.driver.current_url
        self.click_xpath('//div[@data-name="edit"]')
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_contact_two_selected_contact(self):
        old_window_url = self.driver.current_url
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[2]')
        self.click_xpath('//div[@data-name="edit"]')

        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_contact_success(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        new_firstname = "test_firstname2"

        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")
        self.change_firstname_field(firstname, lastname, new_firstname)

        edit_result = self.check_edited_field(new_firstname, lastname)
        self.delete_tested_contact(new_firstname, lastname)
        assert edit_result

    def test_edit_contact_list_success(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        new_firstname = "test_firstname2"

        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")
        self.go_to_contact_list()
        self.change_firstname_field(firstname, lastname, new_firstname, True)
        edit_result = self.check_edited_field(new_firstname, lastname)
        self.delete_tested_contact(new_firstname, lastname)
        assert edit_result

    def test_edit_contact_delete_all_info(self):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')
        old_window_url = self.driver.current_url
        self.fill_contact("", "", "", "", "")
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_contact_wrong_email_cyrillic(self):
        new_email = "ааааыыввы"
        equal_url = self.change_email(new_email)
        assert equal_url

    def test_edit_contact_wrong_email_without_at_sign(self):
        new_email = "fffffffdassa"
        equal_url = self.change_email(new_email)
        assert equal_url

    def test_edit_contact_add_another_email(self):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')

        add_buttons = self.driver.find_elements_by_xpath(
            '//div[@class="form__row__subwidget form__row__subwidget_top-margin form__row__subwidget_first"]//a[text('
            ')=\'Добавить\']')
        add_buttons[0].click()

        new_email = "test" + str(self.random_with_n_digits(1)) + "@mail.com"
        email_input = self.driver.find_elements_by_name("emails")
        email_input[-1].click()
        email_input[-1].clear()
        email_input[-1].send_keys(new_email)

        self.click_xpath('//div[@data-name="submit"]')

        contact_emails = self.driver.find_elements_by_xpath('//a[@class="js-email-address"]')
        assert (contact_emails[-1].text == new_email)

    def test_edit_contact_add_another_phone(self):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')

        add_buttons = self.driver.find_elements_by_xpath(
            '//div[@data-for="phones"]//a[text()=\'Добавить\' and @class="form__row__subwidget_inline form__row__subwidget__control pseudo-link js-add-subwidget"]')
        add_buttons[0].click()

        new_phone = "+" + str(self.random_with_n_digits(5))
        phone_input = self.driver.find_elements_by_name("phones")
        phone_input[-1].click()
        phone_input[-1].clear()
        phone_input[-1].send_keys(new_phone)

        self.click_xpath('//div[@data-name="submit"]')

        contact_phones = self.driver.find_elements_by_xpath('//span[@class="contact__phones__item__value"]')
        assert (contact_phones[-1].text == new_phone)

    def test_edit_contact_add_another_email_button_below(self):
        pass

    def test_edit_contact_add_another_phone_button_below(self):
        pass
