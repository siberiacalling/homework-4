from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class DeleteContactTests(BaseTest):
    TEST_FIRSTNAME = "test_firstname"
    TEST_LASTNAME = "test_lastname"
    TEST_COMPANY = "test_company"
    TEST_EMAIL = "test_email@mail.ru"
    TEST_PHONE = "+12345"

    TEST_FIRSTNAME_ = "test_firstname2"
    TEST_LASTNAME_ = "test_lastname2"
    TEST_COMPANY_ = "test_company2"
    TEST_EMAIL_ = "test_email@mail.ru2"
    TEST_PHONE_ = "+12345222"

    def before_each(self):
        AuthSteps(self.driver).auth()

    def test_try_delete_without_contact(self):
        self.steps = AddressBookSteps(self.driver)
        old_window_url = self.driver.current_url
        self.steps.click_remove_button()
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)
    
    def test_delete_contact_from_card(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.go_to_adressbook_start_page()
        self.steps.click_test_contact_in_list(self.TEST_FIRSTNAME, self.TEST_LASTNAME)
        self.steps.delete_tested_contact_from_contact_card()
        assert not self.steps.is_test_contact_in_list(self.TEST_FIRSTNAME, self.TEST_LASTNAME)
