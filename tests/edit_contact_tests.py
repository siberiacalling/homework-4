from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class EditContactTest(BaseTest):
    UNIQUE_GROUP_NAME = 'new-group-is-unique'
    EXISTING_GROUP_NAME = 'existing-group-name'

    TEST_FIRSTNAME = "test_firstname"
    TEST_LASTNAME = "test_lastname"
    TEST_COMPANY = "test_company"
    TEST_EMAIL = "test_email@mail.ru"
    TEST_PHONE = "+12345"

    NEW_FIRSTNAME = "test_firstname2"

    def before_each(self):
        AuthSteps(self.driver).auth()

    def test_edit_without_selected_contact(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.check_first_checkbox()
        self.steps.check_second_checkbox()
        self.steps.click_edit_button()
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_two_selected_contacts(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.click_edit_button()
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)

    def test_edit_contact_success(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.create_test_contact(self.TEST_FIRSTNAME, self.TEST_LASTNAME, self.TEST_COMPANY, self.TEST_EMAIL,
                                       self.TEST_PHONE)
        self.steps.click_edit_button()
        self.steps.change_firstname_field(self.NEW_FIRSTNAME)
        edit_result = self.steps.check_edited_field(self.NEW_FIRSTNAME, self.TEST_LASTNAME)
        assert edit_result
        self.steps.delete_tested_contact()
