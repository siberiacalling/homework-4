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

    def before_each(self):
        AuthSteps(self.driver).auth()

    def test_successful_add_contact_with_firstname_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, None, None, None, None)
        assert self.steps.check_edited_contact_title(self.TEST_FIRSTNAME, None)
        self.steps.delete_tested_contact_from_contact_card()

    def test_successful_add_contact_with_lastname_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, self.TEST_LASTNAME, None, None, None)
        assert self.steps.check_edited_contact_title(None, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_from_contact_card()

    def test_successful_add_contact_with_company_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, None, self.TEST_COMPANY, None, None)
        assert self.steps.check_edited_contact_title(self.EMPTY_CONTACT_TITLE, None)
        self.steps.delete_tested_contact_from_contact_card()

    def test_successful_add_contact_with_email_only(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(None, None, None, self.TEST_EMAIL, None)
        assert self.steps.email_was_added_successfully(self.TEST_EMAIL) and self.steps.check_edited_contact_title(
            self.EMPTY_CONTACT_TITLE, None)
        self.steps.delete_tested_contact_from_contact_card()

    def test_successful_add_contact(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        assert self.steps.check_edited_contact_title(self.TEST_FIRSTNAME, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_from_contact_card()