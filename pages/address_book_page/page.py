from framework.page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .create_group_popup import CreateGroupPopup
from .edit_group_popup import EditGroupPopup
from .ingroup_dropdown import IngroupDropdown
from .contact_form import ContactForm
from .contact_card import ContactCard


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
        SEND_BUTTON = (By.XPATH, '//div[@data-name="send"]')
        SUBMIT_BUTTON = (By.XPATH, '//div[@data-name="submit"]')

        ADDRESSBOOK_HREF = (By.XPATH, '//a[contains(@href,"/addressbook")]')

        @staticmethod
        def group_container(name: str):
            return (
                By.XPATH,
                f'//span[.="{name}"][@class="menu__item__link__text menu__item__link__text_linear"]/parent::*')

        @staticmethod
        def current_contact_container_in_list(firstname: str, lastname: str):
            return (
                By.XPATH,
                f'//span[text()=\'{lastname} {firstname}\']')

    def open_create_group_popup(self) -> CreateGroupPopup:
        self.wait_for_clickable(*self.Locators.CREATE_GROUP_LINK).click()
        popup = CreateGroupPopup(self.driver)
        popup.check_appear()
        return popup

    def open_edit_form(self) -> ContactForm:
        self.wait_for_clickable(*self.Locators.EDIT_BUTTON).click()
        form = ContactForm(self.driver)
        return form

    def open_add_contact_form(self) -> ContactForm:
        self.wait_for_clickable(*self.Locators.ADD_BUTTON).click()
        form = ContactForm(self.driver)
        return form

    def edit_form(self) -> ContactForm:
        form = ContactForm(self.driver)
        return form

    def contact_card(self) -> ContactCard:
        card = ContactCard(self.driver)
        return card

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

    def click_send_button(self):
        self.wait_for_clickable(*self.Locators.SEND_BUTTON).click()

    def click_add_button(self):
        self.wait_for_clickable(*self.Locators.ADD_BUTTON).click()

    def click_adressbook_href(self):
        self.wait_for_clickable(*self.Locators.ADDRESSBOOK_HREF).click()

    def click_contact_in_list(self, firstname, lastname):
        child_element = self.wait_for_visible(*self.Locators.current_contact_container_in_list(firstname, lastname))
        parent_element = child_element.find_element_by_xpath('..')
        parent_element2 = parent_element.find_element_by_xpath('..')
        parent_element2.click()
