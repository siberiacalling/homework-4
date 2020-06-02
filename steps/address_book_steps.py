from random import randint

from framework.steps import BaseSteps
from pages.address_book_page.page import AddressBookPage


class AddressBookSteps(BaseSteps):
    page: AddressBookPage

    def __init__(self, driver):
        super().__init__(AddressBookPage(driver))

    class TestDataCreation:
        def random_with_n_digits(self, n):
            range_start = 10 ** (n - 1)
            range_end = (10 ** n) - 1
            return randint(range_start, range_end)

        def create_new_phone(self):
            return "+" + str(self.random_with_n_digits(5))

        def create_new_email(self):
            return "test" + str(self.random_with_n_digits(1)) + "@mail.com"

    def create_group_by_link(self, group_name: str):
        popup = self.page.open_create_group_popup()
        popup.fill_group_name_form(group_name)
        popup.confirm()
        popup.check_disappear()

    def create_group_by_link_expecting_error(self, group_name: str):
        popup = self.page.open_create_group_popup()
        popup.fill_group_name_form(group_name)
        popup.confirm()
        popup.check_error()

    def create_group_by_dropdown(self, group_name: str):
        popup = self.page.open_ingroup_dropdown()
        popup.fill_group_name_form(group_name)
        popup.confirm_create_group()

    def delete_group(self, group_name: str):
        popup = self.page.open_edit_group_popup(group_name)
        popup.delete()
        popup.check_disappear()

    def check_first_checkbox(self):
        self.page.check_first_checkbox()

    def check_second_checkbox(self):
        self.page.check_second_checkbox()

    def click_edit_button(self):
        self.page.click_edit_button()

    def add_another_phone(self):
        self.page.click_add_phone_button()
        generator = self.TestDataCreation()
        new_phone = generator.create_new_phone()
        self.page.add_another_field_by_input_name("phones", new_phone)
        self.page.click_submit_button()
        return self.page.phone_was_added_successfully(new_phone)

    def add_another_email(self):
        self.page.click_add_email_button()
        generator = self.TestDataCreation()
        new_email = generator.create_new_email()
        self.page.add_another_field_by_input_name("emails", new_email)
        self.page.click_submit_button()
        return self.page.email_was_added_successfully(new_email)

    def change_email_field(self, new_email):
        self.page.change_email(new_email)
        self.page.click_submit_button()

    def fill_contact_info(self, firstname, lastname, company, email, phone):
        self.page.fill_contact(firstname, lastname, company, email, phone)
        self.page.click_submit_button()

    def create_test_contact(self, firstname, lastname, company, email, phone):
        self.page.click_add_button()
        self.page.fill_contact(firstname, lastname, company, email, phone)
        self.page.click_submit_button()

    def change_firstname_field(self, new_firstname):
        self.page.change_firstname(new_firstname)
        self.page.click_submit_button()

    def edit_current_contact_in_list(self, firstname, lastname):
        self.page.click_contact_in_list(firstname, lastname)
        self.page.click_edit_button()

    def check_edited_field(self, new_firstname, lastname):
        return self.page.check_element_exists_by_xpath(new_firstname, lastname)

    def delete_tested_contact(self):
        self.page.click_remove_button()
        self.page.confirm_remove()

    def go_to_adressbook_start_page(self):
        self.page.click_adressbook_href()
