from random import randint

from framework.steps import BaseSteps
from pages.address_book_page.page import AddressBookPage


class AddressBookSteps(BaseSteps):
    page: AddressBookPage

    def __init__(self, driver):
        super().__init__(AddressBookPage(driver))

    class TestDataGenerator:
        @staticmethod
        def random_with_n_digits(n):
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

    def click_edit_button(self):
        self.page.click_edit_button()

    def click_send_button(self):
        self.page.click_send_button()

    def add_another_email(self):
        generator = self.TestDataGenerator()
        new_email = generator.create_new_email()

        edit_form = self.page.edit_form()
        edit_form.click_add_email_button()

        edit_form.add_another_field_by_input_name("emails", new_email)
        edit_form.click_submit_button()

        contact_card = self.page.contact_card()
        return contact_card.email_was_added_successfully(new_email)

    def change_email_field(self, new_email):
        edit_form = self.page.edit_form()
        edit_form.change_email(new_email)
        edit_form.click_submit_button()

    def fill_contact_info(self, firstname, lastname, company, email, phone):
        edit_form = self.page.edit_form()
        edit_form.fill_contact(firstname, lastname, company, email, phone)
        edit_form.click_submit_button()

    def create_test_contact(self, firstname, lastname, company, email, phone):
        form = self.page.open_add_contact_form()
        form.fill_contact(firstname, lastname, company, email, phone)
        form.click_submit_button()

    def change_firstname_field(self, new_firstname):
        edit_form = self.page.edit_form()
        edit_form.change_firstname(new_firstname)
        edit_form.click_submit_button()

    def edit_current_contact_in_list(self, firstname, lastname):
        self.page.click_contact_in_list(firstname, lastname)
        self.page.click_edit_button()

    def check_edited_field(self, new_firstname, lastname):
        contact_card = self.page.contact_card()
        return contact_card.check_element_exists_by_xpath(new_firstname, lastname)

    def delete_tested_contact_from_contact_card(self):
        contact_card = self.page.contact_card()
        contact_card.click_remove_button()
        contact_card.confirm_remove()

    def go_to_adressbook_start_page(self):
        self.page.click_adressbook_href()

    def edit_first_contact_in_list(self):
        self.page.check_first_checkbox()
        self.page.click_edit_button()

    def edit_two_first_contact_in_list(self):
        self.page.check_first_checkbox()
        self.page.check_second_checkbox()
        self.page.click_edit_button()

    def add_another_phone(self):
        generator = self.TestDataGenerator()
        new_phone = generator.create_new_phone()

        edit_form = self.page.edit_form()
        edit_form.click_add_phone_button()
        edit_form.add_another_field_by_input_name("phones", new_phone)
        edit_form.click_submit_button()

        contact_card = self.page.contact_card()
        return contact_card.phone_was_added_successfully(new_phone)

    def add_another_phone_button_below(self):
        generator = self.TestDataGenerator()
        new_phone = generator.create_new_phone()

        edit_form = self.page.edit_form()
        edit_form.choose_field_button_below('Телефон')
        edit_form.add_another_field_by_input_name("phones", new_phone)
        edit_form.click_submit_button()
        return new_phone

    def add_job_title_button_below(self, job_title):
        edit_form = self.page.open_edit_form()
        edit_form.choose_field_button_below('Должность')
        edit_form.add_another_field_by_input_name("job_title", job_title)
        edit_form.click_submit_button()

    def add_boss_button_below(self, boss):
        edit_form = self.page.open_edit_form()
        edit_form.choose_field_button_below('Руководитель')
        edit_form.add_another_field_by_input_name("boss", boss)
        edit_form.click_submit_button()

    def add_nick_button_below(self, nick):
        edit_form = self.page.open_edit_form()
        edit_form = self.page.edit_form()
        edit_form.choose_field_button_below('Псевдоним')
        edit_form.add_another_field_by_input_name("nick", nick)
        edit_form.click_submit_button()

    def boss_was_added_successfully(self, boss):
        contact_card = self.page.contact_card()
        return contact_card.boss_was_added_successfully(boss)

    def nick_was_added_successfully(self, nick):
        contact_card = self.page.contact_card()
        return contact_card.nick_was_added_successfully(nick)

    def gender_was_added_successfully(self):
        contact_card = self.page.contact_card()
        return contact_card.gender_was_added_successfully()

    def phone_was_added_successfully(self, new_phone):
        contact_card = self.page.contact_card()
        return contact_card.phone_was_added_successfully(new_phone)

    def job_title_was_added_successfully(self, job_title):
        contact_card = self.page.contact_card()
        return contact_card.job_title_was_added_successfully(job_title)

    def add_gender_button_below(self):
        edit_form = self.page.open_edit_form()
        edit_form.choose_field_button_below('Пол')
        edit_form.click_male_gender()
        edit_form.click_submit_button()

    def delete_job_title(self):
        form = self.page.open_edit_form()
        form.click_delete_button_job_title()
        form.click_submit_button()

    def delete_boss(self):
        edit_form = self.page.open_edit_form()
        edit_form.click_delete_button_boss()
        edit_form.click_submit_button()

    def delete_nick(self):
        edit_form = self.page.open_edit_form()
        edit_form.click_delete_button_nick()
        edit_form.click_submit_button()

    def nick_was_deleted(self):
        contact_card = self.page.contact_card()
        return contact_card.nick_was_deleted()

    def boss_was_deleted(self):
        contact_card = self.page.contact_card()
        return contact_card.boss_was_deleted()

    def job_title_was_deleted(self):
        contact_card = self.page.contact_card()
        return contact_card.job_title_was_deleted()

    def select_one_contact_from_list(self):
        self.page.check_first_checkbox()

    def select_two_contacts_from_list(self):
        self.page.check_first_checkbox()
        self.page.check_second_checkbox()

