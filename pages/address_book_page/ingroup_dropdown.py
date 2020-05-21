from framework.page import BasePage
from selenium.webdriver.common.by import By


class IngroupDropdown(BasePage):
    class Locators:
        CONTAINER = ()
        NEW_GROUP_FORM = (By.CSS_SELECTOR, 'input.dropdown__list__new-item__input.form__field.js-add-label-to-dropdown-input')
        CONFIRM_CREATE_GROUP_BTN = (By.CSS_SELECTOR, 'button.dropdown__list__new-item__button.btn.btn_stylish'
                                                     '.js-add-label-to-dropdown-button.dropdown__list__new-item__button')

    def fill_group_name_form(self, name: str):
        group_form = self.wait_for_clickable(*self.Locators.NEW_GROUP_FORM)
        group_form.send_keys(name)

    def confirm_create_group(self):
        self.wait_for_clickable(*self.Locators.CONFIRM_CREATE_GROUP_BTN).click()
