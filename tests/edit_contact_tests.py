from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class EditContactTest(BaseTest):
    TEST_FIRSTNAME = "test_firstname"
    TEST_LASTNAME = "test_lastname"
    TEST_COMPANY = "test_company"
    TEST_EMAIL = "test_email@mail.ru"
    TEST_PHONE = "+12345"
    TEST_JOB_TITLE = "test_job_title"
    TEST_BOSS = "test_boss"
    TEST_NICK = "test_nick"

    EMAIL_WITHOUT_AT_SIGN = "fffffffdassa"
    EMAIL_CYRILLIC = "ааааыыввы"
    NEW_FIRSTNAME = "test_firstname2"

    def before_each(self):
        AuthSteps(self.driver).auth()

    def test_edit_without_selected_contact(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.click_edit_button()
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_two_selected_contacts(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_two_first_contact_in_list()
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_contact_success(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.click_edit_button()
        self.steps.change_firstname_field(self.NEW_FIRSTNAME)
        edit_result = self.steps.check_edited_contact_title(self.NEW_FIRSTNAME, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_from_contact_card()
        assert edit_result

    def test_edit_contact_list_success(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.go_to_adressbook_start_page()
        self.steps.edit_current_contact_in_list(self.TEST_FIRSTNAME, self.TEST_LASTNAME)
        self.steps.change_firstname_field(self.NEW_FIRSTNAME)
        edit_result = self.steps.check_edited_contact_title(self.NEW_FIRSTNAME, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_from_contact_card()
        assert edit_result

    def test_delete_all_info(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        old_window_url = self.driver.current_url
        self.steps.fill_contact_info("", "", "", "", "")
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_wrong_email_cyrillic(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        old_window_url = self.driver.current_url
        self.steps.change_email_field(self.EMAIL_CYRILLIC)
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_wrong_email_without_at_sign(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        old_window_url = self.driver.current_url
        self.steps.change_email_field(self.EMAIL_WITHOUT_AT_SIGN)
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_add_another_phone(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        assert self.steps.add_another_phone()

    def test_add_another_email(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        assert self.steps.add_another_email()

    def test_add_another_phone_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        new_phone = self.steps.add_another_phone_button_below()
        assert self.steps.phone_was_added_successfully(new_phone)

    def test_add_another_email_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.edit_first_contact_in_list()
        new_email = self.steps.add_another_email_button_below()
        assert self.steps.email_was_added_successfully(new_email)

    def test_add_job_title_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_job_title_button_below(self.TEST_JOB_TITLE)
        assert self.steps.job_title_was_added_successfully(self.TEST_JOB_TITLE)
        self.steps.delete_tested_contact_from_contact_card()

    def test_add_boss_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_boss_button_below(self.TEST_BOSS)
        assert self.steps.boss_was_added_successfully(self.TEST_BOSS)
        self.steps.delete_tested_contact_from_contact_card()

    def test_add_nick_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_nick_button_below(self.TEST_NICK)
        assert self.steps.nick_was_added_successfully(self.TEST_NICK)
        self.steps.delete_tested_contact_from_contact_card()

    def test_add_gender_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_gender_button_below()
        assert self.steps.gender_was_added_successfully()
        self.steps.delete_tested_contact_from_contact_card()

    def test_delete_job_title(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_job_title_button_below(self.TEST_JOB_TITLE)
        self.steps.delete_job_title()
        assert self.steps.job_title_not_on_page()
        self.steps.delete_tested_contact_from_contact_card()

    def test_delete_boss(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_boss_button_below(self.TEST_BOSS)
        self.steps.delete_boss()
        assert self.steps.boss_not_on_page()
        self.steps.delete_tested_contact_from_contact_card()

    def test_delete_nick(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.add_nick_button_below(self.TEST_NICK)
        self.steps.delete_nick()
        assert self.steps.nick_not_on_page()
        self.steps.delete_tested_contact_from_contact_card()
