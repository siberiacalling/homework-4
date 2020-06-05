from random import randint

from framework.steps import BaseSteps
from pages.address_book_page.page import AddressBookPage
from .data_generator import DataGenerator


class AddressBookSteps(BaseSteps):
    page: AddressBookPage

    BUTTON_BELOW_TEXT_JOB_TITLE = 'Должность'
    BUTTON_BELOW_TEXT_PHONE = 'Телефон'
    BUTTON_BELOW_TEXT_GENDER = 'Пол'
    BUTTON_BELOW_TEXT_NICK = 'Псевдоним'
    BUTTON_BELOW_TEXT_EMAIL = 'E-mail'
    BUTTON_BELOW_TEXT_BOSS = 'Руководитель'
    BUTTON_BELOW_TEXT_ADDRESS = 'Адрес'

    EMAIL_INPUT_NAME = "emails"
    BOSS_INPUT_NAME = "boss"
    NICK_INPUT_NAME = "nick"
    JOB_TITLE_INPUT_NAME = "job_title"
    PHONE_INPUT_NAME = "phones"
    ADDRESS_INPUT_NAME = "address"

    TEST_JOB_TITLE = "test_job_title"
    TEST_BOSS = "test_boss"
    TEST_NICK = "test_nick"
    TEST_ADDRESS = "Moscow"

    def __init__(self, driver):
        super().__init__(AddressBookPage(driver))

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
        generator = DataGenerator()
        new_email = generator.create_new_email()

        edit_form = self.page.edit_form()
        edit_form.click_add_email_button()
        edit_form.add_another_field_by_input_name(self.EMAIL_INPUT_NAME, new_email)
        edit_form.click_submit_button()

        contact_card = self.page.contact_card()
        return contact_card.email_was_added_successfully(new_email)

    def email_was_added_successfully(self, email):
        contact_card = self.page.contact_card()
        return contact_card.email_was_added_successfully(email)

    def change_email_field(self, new_email):
        edit_form = self.page.edit_form()
        edit_form.change_email(new_email)
        edit_form.click_submit_button()

    def fill_contact_info(self, firstname, lastname, company, email, phone):
        edit_form = self.page.edit_form()
        edit_form.fill_contact(firstname, lastname, company, email, phone)
        edit_form.click_submit_button()

    def process_create_contact_fields(self, another_field, button_below):
        form = self.page.edit_form()
        success = False
        if another_field == "email" and not button_below:
            generator = DataGenerator()
            new_email = generator.create_new_email()

            form.click_add_email_button()
            form.add_another_field_by_input_name(self.EMAIL_INPUT_NAME, new_email)
            form.click_submit_button()
            contact_card = self.page.contact_card()
            success = contact_card.email_was_added_successfully(new_email)
        elif another_field == "phone" and not button_below:
            generator = DataGenerator()
            new_phone = generator.create_new_email()

            form.click_add_phone_button()
            form.add_another_field_by_input_name(self.PHONE_INPUT_NAME, new_phone)
            form.click_submit_button()
            contact_card = self.page.contact_card()
            success = contact_card.phone_was_added_successfully(new_phone)
        elif another_field == "phone" and button_below:
            new_phone = self.add_another_phone_button_below()
            success = self.phone_was_added_successfully(new_phone)
        elif another_field == "email" and button_below:
            new_email = self.add_another_email_button_below()
            success = self.email_was_added_successfully(new_email)
        elif another_field == "nick" and button_below:
            self.add_nick_button_below(self.TEST_NICK, False)
            success = self.nick_was_added_successfully(self.TEST_NICK)
        elif another_field == "job_title" and button_below:
            self.add_job_title_button_below(self.TEST_JOB_TITLE, False)
            success = self.job_title_was_added_successfully(self.TEST_JOB_TITLE)
        elif another_field == "boss" and button_below:
            self.add_boss_button_below(self.TEST_BOSS, False)
            success = self.boss_was_added_successfully(self.TEST_BOSS)
        elif another_field == "gender" and button_below:
            self.add_gender_button_below(False)
            success = self.gender_was_added_successfully()
        elif another_field == "address" and button_below:
            self.add_address_button_below(self.TEST_ADDRESS, False)
            success = self.address_was_added_successfully(self.TEST_ADDRESS)
        elif another_field == "address" and button_below:
            self.add_address_button_below(self.TEST_ADDRESS, False)
            success = self.address_was_added_successfully(self.TEST_ADDRESS)
        return success

    def add_field(self, field):
        if field == "job_title":
            self.add_job_title_button_below(self.TEST_JOB_TITLE, False, False)
        elif field == "boss":
            self.add_boss_button_below(self.TEST_BOSS, False, False)
        elif field == "nick":
            self.add_nick_button_below(self.TEST_NICK, False, False)

    def delete_field(self, field):
        if field == "job_title":
            self.delete_job_title(False)
            return self.job_title_not_on_page()

    def create_test_contact(self, firstname, lastname, company, email, phone, another_field=None, button_below=False):
        success = False
        form = self.page.open_add_contact_form()
        form.fill_contact(firstname, lastname, company, email, phone)
        if not another_field and not button_below:
            form.click_submit_button()
        else:
            success = self.process_create_contact_fields(another_field, button_below)
        return success

    def create_test_contact_with_field_delete(self, firstname, lastname, company, email, phone, another_field):
        form = self.page.open_add_contact_form()
        form.fill_contact(firstname, lastname, company, email, phone)
        self.add_field(another_field)

        if another_field == "job_title":
            form.click_delete_button_job_title()
            form.click_submit_button()
            return self.job_title_not_on_page()
        elif another_field == "boss":
            self.delete_boss(False)
            return self.boss_not_on_page()
        elif another_field == "nick":
            self.delete_nick(False)
            return self.nick_not_on_page()
        form.click_submit_button()


    def change_firstname_field(self, new_firstname):
        edit_form = self.page.edit_form()
        edit_form.change_firstname(new_firstname)
        edit_form.click_submit_button()

    def edit_current_contact_in_list(self, firstname, lastname):
        self.page.click_contact_in_list(firstname, lastname)
        self.page.click_edit_button()

    def check_edited_contact_title(self, new_firstname, lastname):
        contact_card = self.page.contact_card()
        return contact_card.check_contact_title_by_firstname_and_lastname(new_firstname, lastname)

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
        generator = DataGenerator()
        new_phone = generator.create_new_phone()

        edit_form = self.page.edit_form()
        edit_form.click_add_phone_button()
        edit_form.add_another_field_by_input_name(self.PHONE_INPUT_NAME, new_phone)
        edit_form.click_submit_button()

        contact_card = self.page.contact_card()
        return contact_card.phone_was_added_successfully(new_phone)

    def add_another_phone_button_below(self, submit=True):
        generator = DataGenerator()
        new_phone = generator.create_new_phone()

        edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_PHONE)
        edit_form.add_another_field_by_input_name(self.PHONE_INPUT_NAME, new_phone)
        if submit:
            edit_form.click_submit_button()
        return new_phone

    def add_another_email_button_below(self):
        generator = DataGenerator()
        new_email = generator.create_new_email()

        edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_EMAIL)
        edit_form.add_another_field_by_input_name(self.EMAIL_INPUT_NAME, new_email)
        edit_form.click_submit_button()
        return new_email

    def add_job_title_button_below(self, job_title, open_form=True, save=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_JOB_TITLE)
        edit_form.add_another_field_by_input_name(self.JOB_TITLE_INPUT_NAME, job_title)
        if save:
            edit_form.click_submit_button()

    def add_boss_button_below(self, boss, open_form=True, save=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_BOSS)
        edit_form.add_another_field_by_input_name(self.BOSS_INPUT_NAME, boss)
        if save:
            edit_form.click_submit_button()

    def add_nick_button_below(self, nick, open_form=True, save=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_NICK)
        edit_form.add_another_field_by_input_name(self.NICK_INPUT_NAME, nick)
        if save:
            edit_form.click_submit_button()

    def add_gender_button_below(self, open_form=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_GENDER)
        edit_form.click_male_gender()
        edit_form.click_submit_button()

    def add_address_button_below(self, address, open_form=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.choose_field_button_below(self.BUTTON_BELOW_TEXT_ADDRESS)
        edit_form.add_another_field_by_input_name(self.ADDRESS_INPUT_NAME, address)
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

    def address_was_added_successfully(self, address):
        contact_card = self.page.contact_card()
        return contact_card.address_was_added_successfully(address)

    def phone_was_added_successfully(self, new_phone):
        contact_card = self.page.contact_card()
        return contact_card.phone_was_added_successfully(new_phone)

    def job_title_was_added_successfully(self, job_title):
        contact_card = self.page.contact_card()
        return contact_card.job_title_was_added_successfully(job_title)

    def delete_job_title(self, open_form=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()

        edit_form.click_delete_button_job_title()
        edit_form.click_submit_button()

    def delete_boss(self, open_form=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.click_delete_button_boss()
        edit_form.click_submit_button()

    def delete_nick(self, open_form=True):
        if open_form:
            edit_form = self.page.open_edit_form()
        else:
            edit_form = self.page.edit_form()
        edit_form.click_delete_button_nick()
        edit_form.click_submit_button()

    def nick_not_on_page(self):
        contact_card = self.page.contact_card()
        return contact_card.nick_not_on_page()

    def boss_not_on_page(self):
        contact_card = self.page.contact_card()
        return contact_card.boss_not_on_page()

    def job_title_not_on_page(self):
        contact_card = self.page.contact_card()
        return contact_card.job_title_not_on_page()

    def select_one_contact_from_list(self):
        self.page.check_first_checkbox()

    def select_two_contacts_from_list(self):
        self.page.check_first_checkbox()
        self.page.check_second_checkbox()
