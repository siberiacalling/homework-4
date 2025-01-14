from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class AddContactTests(BaseTest):
    TEST_FIRSTNAME = "test_firstname"
    TEST_LASTNAME = "test_lastname"
    TEST_COMPANY = "test_company"
    TEST_EMAIL = "test_email@mail.ru"
    TEST_PHONE = "+12345"
    TEST_JOB_TITLE = "test_job_title"
    TEST_BOSS = "test_boss"
    TEST_NICK = "test_nick"

    EMPTY_CONTACT_TITLE = "- контакт без названия -"
    EMAIL_WITHOUT_AT_SIGN = "fffffffdassa"
    EMAIL_CYRILLIC = "ааааыыввы"

    ADD_CONTACT_URL = "https://e.mail.ru/addressbook/add"

    def before_each(self):
        AuthSteps(self.driver).auth()

    def test_cancel_add_contact(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.open_add_contact_form()
        old_url = self.driver.current_url
        self.steps.click_reset_button()
        new_url = self.driver.current_url
        assert (old_url != new_url)

    def test_successful_add_contact_with_firstname_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, None, None, None, None)
        assert self.steps.check_edited_contact_title(self.TEST_FIRSTNAME, None)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_with_lastname_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, self.TEST_LASTNAME, None, None, None)
        assert self.steps.check_edited_contact_title(None, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_with_company_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, None, self.TEST_COMPANY, None, None)
        assert self.steps.check_edited_contact_title(self.EMPTY_CONTACT_TITLE, None)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_with_email_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, None, None, self.TEST_EMAIL, None)
        assert self.steps.email_was_added_successfully(self.TEST_EMAIL) and self.steps.check_edited_contact_title(
            self.EMPTY_CONTACT_TITLE, None)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        assert self.steps.check_edited_contact_title(self.TEST_FIRSTNAME, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_and_confirm()

    def test_try_to_add_empty_contact(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact("", "", "", "", "")
        window_url = self.driver.current_url
        assert (window_url == self.ADD_CONTACT_URL)

    def test_successful_add_contact_with_email_without_at_sign(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, None, None, self.EMAIL_WITHOUT_AT_SIGN, None)
        window_url = self.driver.current_url
        assert (window_url == self.ADD_CONTACT_URL)

    def test_successful_add_contact_with_email_cyrillic(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, None, None, self.EMAIL_CYRILLIC, None)
        window_url = self.driver.current_url
        assert (window_url == self.ADD_CONTACT_URL)

    def test_successful_add_contact_another_email(self):
        self.steps = AddressBookSteps(self.driver)
        success = self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                                 self.TEST_EMAIL,
                                                 self.TEST_PHONE, "email")
        assert success
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_another_phone(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "phone")
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_phone_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "phone", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_another_email_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "email", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_nick_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "nick", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_job_title_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "job_title", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_boss_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "boss", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_gender_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "gender", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_add_contact_address_button_below(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY,
                                              self.TEST_EMAIL,
                                              self.TEST_PHONE, "address", True)
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_delete_job_title_during_creation(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact_with_field_delete(self.TEST_FIRSTNAME, self.TEST_LASTNAME,
                                                                self.TEST_COMPANY,
                                                                self.TEST_EMAIL,
                                                                self.TEST_PHONE, "job_title")
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_delete_boss_during_creation(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact_with_field_delete(self.TEST_FIRSTNAME, self.TEST_LASTNAME,
                                                                self.TEST_COMPANY,
                                                                self.TEST_EMAIL,
                                                                self.TEST_PHONE, "boss")
        self.steps.delete_tested_contact_and_confirm()

    def test_successful_delete_nick_during_creation(self):
        self.steps = AddressBookSteps(self.driver)
        assert self.steps.create_test_contact_with_field_delete(self.TEST_FIRSTNAME, self.TEST_LASTNAME,
                                                                self.TEST_COMPANY,
                                                                self.TEST_EMAIL,
                                                                self.TEST_PHONE, "nick")
        self.steps.delete_tested_contact_and_confirm()
