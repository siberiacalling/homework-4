# coding=utf-8
import time as t
from datetime import datetime
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .page import Page


class AddressBookPage(Page):
    def click_xpath(self, xpath):
        element = WebDriverWait(self.driver, 150).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
            #EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def click_element_in_array_xpath(self, xpath, index):
        button_in_list = WebDriverWait(self.driver, 150).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath)))
        button_in_list[index].click()

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
        child_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

        # child_element = self.driver.find_element_by_xpath(xpath)
        parent_element = child_element.find_element_by_xpath('..')
        parent_element2 = parent_element.find_element_by_xpath('..')
        parent_element2.click()

    def delete_tested_contact(self, firstname, lastname):
        # self.click_contact_in_list(firstname, lastname)
        self.click_xpath('//div[@data-name="remove"]')
        # remove_button = WebDriverWait(self.driver, 35).until(
        # EC.element_to_be_clickable((By.XPATH, '//div[@data-name="remove"]')))
        # remove_button.click()

        self.click_element_in_array_xpath('//*[contains(@class, \'btn btn_main confirm-ok\')]', 0)
        # confirm_button = self.driver.find_elements_by_xpath('//*[contains(@class, \'btn btn_main confirm-ok\')]')
        # confirm_button[0].click()

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
            # button = WebDriverWait(self.driver, 35).until(
            # EC.element_to_be_clickable((By.XPATH, '//div[@data-name="edit"]')))
            # button.click()

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
        self.click_xpath('//a[contains(@href,"/addressbook")]')
        # contacts = self.driver.find_element_by_xpath('//a[contains(@href,"/addressbook")]')
        # contacts.click()

    def change_email(self, new_email):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')
        old_window_url = self.driver.current_url
        self.change_email_field(new_email)
        new_window_url = self.driver.current_url
        return old_window_url == new_window_url

    def add_another_field_by_input_name(self, name, new_field):
        email_input = self.driver.find_elements_by_name(name)
        email_input[-1].click()
        email_input[-1].clear()
        email_input[-1].send_keys(new_field)
        self.click_xpath('//div[@data-name="submit"]')

    def create_new_email(self):
        return "test" + str(self.random_with_n_digits(1)) + "@mail.com"

    def create_new_phone(self):
        return "+" + str(self.random_with_n_digits(5))

    def edit_first_contact_from_list(self):
        self.click_xpath('(//input[@class="messageline__checkbox__input"])[1]')
        self.click_xpath('//div[@data-name="edit"]')

    def choose_field_button_below(self, field_name):
        xpath = '//span[text()=\'Добавить поле\']'
        child_element = self.driver.find_elements_by_xpath(xpath)
        parent_element = child_element[0].find_element_by_xpath('..')
        parent_element.click()

        self.click_element_in_array_xpath(
            '//ul[@class="form__dropdown__list form__dropdown__list_limit filters__dropdown__menu js-menu"]//a[text('
            ')=\'' + field_name + '\']', 1)
        # button_in_list = WebDriverWait(self.driver, 35).until(
        # EC.presence_of_all_elements_located((By.XPATH,
        # '//ul[@class="form__dropdown__list form__dropdown__list_limit filters__dropdown__menu js-menu"]//a[text('
        # ')=\'' + field_name + '\']')))
        # layout bug
        # button_in_list[1].click()

    def delete_field(self, delete_button_xpath, check_path):
        self.click_xpath('//div[@data-name="edit"]')
        # button = WebDriverWait(self.driver, 35).until(
        # EC.element_to_be_clickable((By.XPATH, '//div[@data-name="edit"]')))
        # button.click()
        self.click_element_in_array_xpath(delete_button_xpath, 0)
        # delete_button = WebDriverWait(self.driver, 35).until(
        # EC.presence_of_all_elements_located((By.XPATH, delete_button_xpath)))

        # delete_button[0].click()
        self.click_xpath('//div[@data-name="submit"]')
        value_in_contact_card = self.driver.find_elements_by_xpath(check_path)
        if not value_in_contact_card:
            return True
        return False

    def add_single_field(self, field_name, input_name, new_value):
        self.click_element_in_array_xpath('//div[@data-name="edit"]', 0)

        # edit_buttons = self.driver.find_elements_by_xpath('//div[@data-name="edit"]')
        # edit_buttons[0].click()

        self.choose_field_button_below(field_name)
        self.add_another_field_by_input_name(input_name, new_value)
        self.click_xpath('//div[@data-name="submit"]')

    # ~~~~~~~~~~~~~~~~~~~~~~~TESTS~~~~~~~~~~~~~~~~~~~~~~
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
        self.click_xpath('//div[@data-name="edit"]')
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
        self.edit_first_contact_from_list()

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
        self.edit_first_contact_from_list()

        self.click_element_in_array_xpath(
            '//div[@class="form__row__subwidget form__row__subwidget_top-margin form__row__subwidget_first"]//a[text('
            ')=\'Добавить\']', 0)
        # add_buttons = self.driver.find_elements_by_xpath(
        # '//div[@class="form__row__subwidget form__row__subwidget_top-margin form__row__subwidget_first"]//a[text('
        # ')=\'Добавить\']')
        # add_buttons[0].click()

        new_email = self.create_new_email()
        self.add_another_field_by_input_name("emails", new_email)

        contact_emails = self.driver.find_elements_by_xpath('//a[@class="js-email-address"]')
        assert (contact_emails[-1].text == new_email)

    def test_edit_contact_add_another_phone(self):
        self.edit_first_contact_from_list()
        self.click_element_in_array_xpath(
            '//div[@data-for="phones"]//a[text()=\'Добавить\' and @class="form__row__subwidget_inline '
            'form__row__subwidget__control pseudo-link js-add-subwidget"]', 0)

        # add_buttons = self.driver.find_elements_by_xpath(
        # '//div[@data-for="phones"]//a[text()=\'Добавить\' and @class="form__row__subwidget_inline '
        # 'form__row__subwidget__control pseudo-link js-add-subwidget"]')
        # add_buttons[0].click()

        new_phone = self.create_new_phone()
        self.add_another_field_by_input_name("phones", new_phone)

        contact_phones = self.driver.find_elements_by_xpath('//span[@class="contact__phones__item__value"]')
        assert (contact_phones[-1].text == new_phone)

    def test_edit_contact_add_another_email_button_below(self):
        self.edit_first_contact_from_list()
        self.choose_field_button_below('E-mail')

        new_email = self.create_new_email()
        self.add_another_field_by_input_name("emails", new_email)

        contact_emails = self.driver.find_elements_by_xpath('//a[@class="js-email-address"]')
        assert (contact_emails[-1].text == new_email)

    def test_edit_contact_add_another_phone_button_below(self):
        self.edit_first_contact_from_list()
        self.choose_field_button_below('Телефон')

        new_phone = self.create_new_phone()
        self.add_another_field_by_input_name("phones", new_phone)

        contact_phones = self.driver.find_elements_by_xpath('//span[@class="contact__phones__item__value"]')
        assert (contact_phones[-1].text == new_phone)

    def test_single_input(self, field_name, input_name, new_value, xpath_for_checking, check_value=None,
                          boss_check=False):
        self.click_xpath('//div[@data-name="edit"]')
        #button = WebDriverWait(self.driver, 35).until(
            #EC.element_to_be_clickable((By.XPATH, '//div[@data-name="edit"]')))
        #button.click()

        self.choose_field_button_below(field_name)

        self.add_another_field_by_input_name(input_name, new_value)
        value_in_contact_card = self.driver.find_elements_by_xpath(xpath_for_checking)

        if not boss_check:
            page_value = value_in_contact_card[-1].text
        else:
            page_value = value_in_contact_card[-1].text.split()[1]

        if check_value:
            return page_value == check_value
        return page_value == new_value

    def test_edit_contact_add_nick_button_below(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")

        new_value = 'test_nick'
        check_value = '«' + new_value + '»'
        assert self.test_single_input('Псевдоним', 'nick', new_value,
                                      '//span[@class="contact__header__title__additional"]', check_value)
        self.delete_tested_contact(firstname, lastname)

    def test_edit_contact_add_job_title_button_below(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")

        assert self.test_single_input('Должность', 'job_title', 'test_job_title',
                                      '//span[@class="contact__job__item contact__job__item_job_title"]')
        self.delete_tested_contact(firstname, lastname)

    def test_edit_contact_add_boss_button_below(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")

        assert self.test_single_input('Руководитель', 'boss', 'test_boss',
                                      '//div[@class="contact__job__item contact__job__item_boss"]', None, True)
        self.delete_tested_contact(firstname, lastname)

    def test_edit_contact_delete_job_title(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")

        self.add_single_field('Должность', 'job_title', 'test_job_title')
        assert self.delete_field('//div[@data-for="job_title"]//a[@title="Удалить"]',
                                 '//span[@class="contact__job__item contact__job__item_job_title"]')
        self.delete_tested_contact(firstname, lastname)

    def test_edit_contact_delete_boss(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")

        self.add_single_field('Руководитель', 'boss', 'test_boss')
        assert self.delete_field('//div[@data-for="boss"]//a[@title="Удалить"]',
                                 '//div[@class="contact__job__item contact__job__item_boss"]')
        self.delete_tested_contact(firstname, lastname)

    def test_edit_contact_delete_nick(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")

        self.add_single_field('Псевдоним', 'nick', 'test_nick')
        assert self.delete_field('//div[@data-for="nick"]//a[@title="Удалить"]',
                                 '//span[@class="contact__header__title__additional"]')
        self.delete_tested_contact(firstname, lastname)

    def test_edit_contact_add_gender_button_below(self):
        firstname = "test_firstname"
        lastname = "test_lastname"
        self.create_test_contact(firstname, lastname, "test_company", "test_email@mail.ru", "+12345")
        self.click_xpath('//div[@data-name="edit"]')

        self.choose_field_button_below('Пол')
        self.click_element_in_array_xpath('//input[@name="sex"]', 0)

        #elements = self.driver.find_elements_by_xpath('//input[@name="sex"]')
        #elements[0].click()
        self.click_xpath('//div[@data-name="submit"]')

        value_in_contact_card = self.driver.find_elements_by_xpath('//div[@class="contact__header__additional"]')
        self.delete_tested_contact(firstname, lastname)
        assert value_in_contact_card[0].text == 'Мужской'
