from framework.page import BasePage, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class CreateGroupPopupPage(BasePage):
    class Locators:
        CONTAINER = (By.ID, 'MailRuConfirm')
        GROUP_FORM = (By.ID, 'label')
        CONFIRM_BTN = (By.CSS_SELECTOR, 'button.btn.btn_main.confirm-ok[data-blockid="btn"]')
        ERROR_LABEL = (By.CSS_SELECTOR, 'popup__desc.popup__desc_messagebox.form__message_error.js-formError')

    def check_appear(self):
        self.wait_for_visible(*self.Locators.CONTAINER)

    def fill_group_name_form(self, name: str):
        group_form = self.wait_for_clickable(*self.Locators.GROUP_FORM)
        group_form.send_keys(name)

    def confirm(self):
        btn = self.wait_for_clickable(*self.Locators.CONFIRM_BTN)
        btn.click()

    def check_error(self):
        self.wait_for_visible(*self.Locators.ERROR_LABEL)

    def check_disappear(self):
        self.wait_for_invisible(*self.Locators.CONTAINER)


class EditGroupPopupPage(BasePage):
    class Locators:
        CONTAINER = (By.ID, 'MailRuConfirm')
        CONFIRM_BTN = (By.CSS_SELECTOR, 'button.btn.btn_main.confirm-ok[data-blockid="btn"]')
        CANCEL_BTN = (By.CSS_SELECTOR, 'button.btn.confirm-cancel[data-blockid="btn"]')
        DELETE_BTN = (By.CSS_SELECTOR, 'a.form__button.form__button_reset.popup__link-removelink.js-remove-label')
        CONFIRM_DELETE_BTN = (By.XPATH, '//button/span[.="Удалить"]')

    def check_appear(self):
        self.wait_for_visible(*self.Locators.CONTAINER)

    def save(self):
        self.__click(*self.Locators.CONFIRM_BTN)

    def cancel(self):
        self.__click(*self.Locators.CANCEL_BTN)

    def delete(self):
        self.__click(*self.Locators.DELETE_BTN)
        self.__click(*self.Locators.CONFIRM_DELETE_BTN)

    def __click(self, by, value):
        self.wait_for_clickable(by, value).click()

    def check_disappear(self):
        self.wait_for_invisible(*self.Locators.CONTAINER)


class AddressBookPage(BasePage):
    class Locators:
        CREATE_GROUP_LINK = (By.CSS_SELECTOR, 'a.menu__option__link.js-add-label')
        EDIT_GROUP_ICON = (By.CSS_SELECTOR,
                           '.icon.icon_right.js-edit-label.icon_folders.'
                           'icon_menu_addressbook.icon_menu_addressbook_edit')

        @staticmethod
        def edit_group_link(name: str):
            return (By.XPATH, f'//span[.="{name}"][@class="menu__item__link__text menu__item__link__text_linear"]')

    def open_create_group_popup(self) -> CreateGroupPopupPage:
        self.wait_for_clickable(*self.Locators.CREATE_GROUP_LINK).click()
        popup = CreateGroupPopupPage(self.driver)
        popup.check_appear()
        return popup

    def open_edit_group_popup(self, group_name: str) -> EditGroupPopupPage:
        group_container: WebElement = self.wait_for_visible(*self.Locators.edit_group_link(group_name)).parent
        edit_icon = group_container.find_element(*self.Locators.EDIT_GROUP_ICON)

        ActionChains(self.driver).move_to_element(edit_icon).click(edit_icon).perform()

        popup = EditGroupPopupPage(self.driver)
        popup.check_appear()
        return popup
