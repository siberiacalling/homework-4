from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class WriteLetterTests(BaseTest):

    def before_each(self):
        AuthSteps(self.driver).auth()

    def test_successful_redirect_one_selected_contact(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.select_one_contact_from_list()
        self.steps.click_send_button()
        new_window_url = self.driver.current_url
        assert (new_window_url != old_window_url)

    def test_successful_redirect_two_selected_contact(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.select_two_contacts_from_list()
        self.steps.click_send_button()
        new_window_url = self.driver.current_url
        assert (new_window_url != old_window_url)

    def test_try_write_letter_without_selected_contact(self):
        old_window_url = self.driver.current_url
        self.steps = AddressBookSteps(self.driver)
        self.steps.click_send_button()
        new_window_url = self.driver.current_url
        assert (new_window_url == old_window_url)
