from framework.steps import BaseSteps
from pages.address_book_page.page import AddressBookPage


class AddressBookSteps(BaseSteps):
    page: AddressBookPage

    def __init__(self, driver):
        super().__init__(AddressBookPage(driver))

    def create_group_by_link(self, group_name: str):
        popup = self.page.open_create_group_popup()
        popup.fill_group_name_form(group_name)
        popup.confirm()
        popup.check_disappear()

    def create_group_by_link_expecting_error(self, group_name: str):
        popup = self.page.open_create_group_popup()
        popup.fill_group_name_form(group_name)
        popup.confirm()
        popup.check_error()

    def create_group_by_dropdown(self, group_name: str):
        popup = self.page.open_ingroup_dropdown()
        popup.fill_group_name_form(group_name)
        popup.confirm_create_group()

    def delete_group(self, group_name: str):
        popup = self.page.open_edit_group_popup(group_name)
        popup.delete()
        popup.check_disappear()

    def check_first_checkbox(self):
        self.page.check_first_checkbox()

    def check_second_checkbox(self):
        self.page.check_second_checkbox()

    def click_edit_button(self):
        self.page.click_edit_button()

    def create_test_contact(self, firstname, lastname, company, email, phone):
        self.page.click_add_button()
        self.page.fill_contact(firstname, lastname, company, email, phone)
        self.page.click_submit_button()

    def change_firstname_field(self, new_firstname):
        self.page.change_firstname(new_firstname)
        self.page.click_submit_button()

    def check_edited_field(self, new_firstname, lastname):
        xpath = '//*[contains(text(), \'' + lastname + " " + new_firstname  + '\')]'
        return self.page.check_element_exists_by_xpath(xpath)

    def delete_tested_contact(self):
        self.page.click_remove_button()
        self.page.confirm_remove()

