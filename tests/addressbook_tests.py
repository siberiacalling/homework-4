# coding=utf-8

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.addressbook_page import AddressBookPage
from pages.authentication_page import AuthPage
from pages.email_page import EmailPage


class AddressBookTests(unittest.TestCase):
    BROWSER_NAME = os.getenv('SELENIUM_TEST_BROWSER', 'CHROME')

    MAIL_URL = 'https://mail.ru/'
    ADDRESSBOOK_URL = 'https://e.mail.ru/addressbook'
    EMAIL_URL = 'https://e.mail.ru/messages/inbox/'

    EMAIL = 'smirnovasiberia'
    PASSWORD = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, self.BROWSER_NAME).copy()
        )

        self.driver.implicitly_wait(50)
        self.page = AuthPage(self.MAIL_URL, self.driver)
        self.page.open()
        self.page.get_form_component.authenticate(self.EMAIL, self.PASSWORD)

        self.page = EmailPage(self.EMAIL_URL, self.driver)
        self.page.switch_to_address_book()

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.page = AddressBookPage(self.ADDRESSBOOK_URL, self.driver)

    def tearDown(self):
        self.driver.quit()

    def testSuccessEditContactList(self):
        self.page.test_edit_contact_list_success()

    def testEditWithoutSelectedContact(self):
        self.page.test_edit_contact_two_selected_contact()

    def testEditTwoSelectedContact(self):
        self.page.test_edit_contact_two_selected_contact()

    def testSuccessEditContact(self):
        self.page.test_edit_contact_success()
    
    def testEditContactDeleteAllInfo(self):
        self.page.test_edit_contact_delete_all_info()


