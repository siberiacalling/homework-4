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

        self.driver.implicitly_wait(10)
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


    def testEditContactAddBossButtonBelow(self):
        self.page.test_edit_contact_add_boss_button_below()

    def testEditContactAddJobTitleButtonBelow(self):
        self.page.test_edit_contact_add_job_title_button_below()
    
    def testEditContactAddAnotherPhoneButtonBelow(self):
        self.page.test_edit_contact_add_another_phone_button_below()

    def testSuccessEditContactList(self):
        self.page.test_edit_contact_list_success()

    def testSuccessEditContact(self):
        self.page.test_edit_contact_success()

    def testEditContactDeleteJobTitle(self):
        self.page.test_edit_contact_delete_job_title()

    def testEditContactDeleteNick(self):
        self.page.test_edit_contact_delete_nick()

    def testEditContactDeleteBoss(self):
        self.page.test_edit_contact_delete_boss()

    def testEditContactAddGender(self):
        self.page.test_edit_contact_add_gender_button_below()

    def testEditWithoutSelectedContact(self):
        self.page.test_edit_contact_two_selected_contact()

    def testEditTwoSelectedContact(self):
        self.page.test_edit_contact_two_selected_contact()

    def testEditContactDeleteAllInfo(self):
        self.page.test_edit_contact_delete_all_info()

    def testEditContactWrongEmailCyrillic(self):
        self.page.test_edit_contact_wrong_email_cyrillic()

    def testEditContactWrongEmailWithoutAtSign(self):
        self.page.test_edit_contact_wrong_email_without_at_sign()

    def testEditContactAddAnotherEmail(self):
        self.page.test_edit_contact_add_another_email()

    def testEditContactAddAnotherPhone(self):
        self.page.test_edit_contact_add_another_phone()