from framework.test import BaseTest
from steps.auth_steps import AuthSteps
from steps.address_book_steps import AddressBookSteps


class CreateGroupTest(BaseTest):
    def setUp(self):
        super().setUp()
        AuthSteps(self.driver).auth()

    def test_successful_create_group(self):
        steps = AddressBookSteps(self.driver)
        steps.open_url('https://e.mail.ru/addressbook')
        unique_group_name = 'new-group-is-unique'
        steps.create_group_by_link(unique_group_name)
        steps.delete_group(unique_group_name)
