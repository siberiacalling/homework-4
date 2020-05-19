from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class CreateGroupTest(BaseTest):
    UNIQUE_GROUP_NAME = 'new-group-is-unique'
    EXISTING_GROUP_NAME = 'existing-group-name'

    def setUp(self):
        super().setUp()
        AuthSteps(self.driver).auth()

    def test_successful_create_group_by_link(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.open_url('https://e.mail.ru/addressbook')
        self.steps.create_group_by_link(self.UNIQUE_GROUP_NAME)
        self.steps.delete_group(self.UNIQUE_GROUP_NAME)

    def test_successful_create_group_by_dropdown(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.open_url('https://e.mail.ru/addressbook')
        self.steps.create_group_by_dropdown(self.UNIQUE_GROUP_NAME)
        self.steps.delete_group(self.UNIQUE_GROUP_NAME)

    def test_try_create_group_with_existing_name(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.open_url('https://e.mail.ru/addressbook')
        self.steps.create_group_by_link_expecting_error(self.EXISTING_GROUP_NAME)

    def test_try_create_group_with_empty_name(self):
        self.steps = AddressBookSteps(self.driver)
        self.steps.open_url('https://e.mail.ru/addressbook')
        self.steps.create_group_by_link_expecting_error('')
