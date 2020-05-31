from framework.page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .create_group_popup import CreateGroupPopup
from .edit_group_popup import EditGroupPopup
from .ingroup_dropdown import IngroupDropdown


class AddressBookPage(BasePage):
    class Locators:
        CREATE_GROUP_LINK = (By.CSS_SELECTOR, 'a.menu__option__link.js-add-label')
        EDIT_GROUP_ICON = (By.CSS_SELECTOR,
                           '.icon.icon_right.js-edit-label.icon_folders.'
                           'icon_menu_addressbook.icon_menu_addressbook_edit')
        INGROUP_DROPDOWN_LINK = (By.XPATH, '//span[.="В группу"][@class="b-dropdown__ctrl__text"]')
        FIRST_CONTACT_CHECKBOX = (By.XPATH, '(//input[@class="messageline__checkbox__input"])[1]')
        SECOND_CONTACT_CHECK_BOX = (By.XPATH, '(//input[@class="messageline__checkbox__input"])[2]')

        EDIT_BUTTON = (By.XPATH, '//div[@data-name="edit"]')
        ADD_BUTTON = (By.XPATH, '//div[@data-name="add"]')
        SUBMIT_BUTTON = (By.XPATH, '//div[@data-name="submit"]')
        REMOVE_BUTTON = (By.XPATH, '//div[@data-name="remove"]')
        CONFIRM_BUTTON_ARRAY = (By.XPATH, '//*[contains(@class, \'btn btn_main confirm-ok\')]')

        FIRSTNAME_EDIT_FORM = (By.NAME, 'firstname')
        LASTNAME_EDIT_FORM = (By.NAME, 'lastname')
        COMPANY_EDIT_FORM = (By.NAME, 'company')
        EMAILS_EDIT_FORM = (By.NAME, 'emails')
        FIRST_PHONE_EDIT_FORM = (By.ID, 'phones_0')

        @staticmethod
        def group_container(name: str):
            return (
                By.XPATH,
                f'//span[.="{name}"][@class="menu__item__link__text menu__item__link__text_linear"]/parent::*')

    def open_create_group_popup(self) -> CreateGroupPopup:
        self.wait_for_clickable(*self.Locators.CREATE_GROUP_LINK).click()
        popup = CreateGroupPopup(self.driver)
        popup.check_appear()
        return popup

    def open_edit_group_popup(self, group_name: str) -> EditGroupPopup:
        group_container = self.wait_for_visible(*self.Locators.group_container(group_name))
        edit_icon = group_container.find_element(*self.Locators.EDIT_GROUP_ICON)

        ActionChains(self.driver).move_to_element(edit_icon).click(edit_icon).perform()

        popup = EditGroupPopup(self.driver)
        popup.check_appear()
        return popup

    def open_ingroup_dropdown(self):
        self.wait_for_clickable(*self.Locators.INGROUP_DROPDOWN_LINK).click()
        popup = IngroupDropdown(self.driver)
        return popup

    def check_first_checkbox(self):
        self.wait_for_clickable(*self.Locators.FIRST_CONTACT_CHECKBOX).click()

    def check_second_checkbox(self):
        self.wait_for_clickable(*self.Locators.SECOND_CONTACT_CHECK_BOX).click()

    def click_edit_button(self):
        self.wait_for_clickable(*self.Locators.EDIT_BUTTON).click()

    def click_add_button(self):
        self.wait_for_clickable(*self.Locators.ADD_BUTTON).click()

    def click_submit_button(self):
        self.wait_for_clickable(*self.Locators.SUBMIT_BUTTON).click()

    def click_remove_button(self):
        self.wait_for_clickable(*self.Locators.REMOVE_BUTTON).click()

    def confirm_remove(self):
        button_in_list = self.wait_for_all_elements(*self.Locators.CONFIRM_BUTTON_ARRAY)
        button_in_list[0].click()

    def fill_contact(self, firstname, lastname, company, email, phone):
        self.wait_for_visible(*self.Locators.FIRSTNAME_EDIT_FORM).send_keys(firstname)
        self.wait_for_visible(*self.Locators.LASTNAME_EDIT_FORM).send_keys(lastname)
        self.wait_for_visible(*self.Locators.COMPANY_EDIT_FORM).send_keys(company)
        self.wait_for_visible(*self.Locators.EMAILS_EDIT_FORM).send_keys(email)
        self.wait_for_visible(*self.Locators.FIRST_PHONE_EDIT_FORM).send_keys(phone)

    def change_firstname(self, new_firstname):
        firstname_field = self.wait_for_visible(*self.Locators.FIRSTNAME_EDIT_FORM)
        firstname_field.click()
        firstname_field.clear()
        firstname_field.send_keys(new_firstname)

    def check_element_exists_by_xpath(self, xpath):
        child_element = self.driver.find_elements_by_xpath(xpath)
        if child_element:
            return True
        return False
