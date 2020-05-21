from framework.page import BasePage
from selenium.webdriver.common.by import By


class CreateGroupPopup(BasePage):
    class Locators:
        CONTAINER = (By.CSS_SELECTOR, '.popup.js-layer.popup_dark.popup_')
        GROUP_FORM = (By.ID, 'label')
        CONFIRM_BTN = (By.CSS_SELECTOR, 'button.btn.btn_main.confirm-ok[data-blockid="btn"]')
        ERROR_LABEL = (By.CSS_SELECTOR, '.popup__desc.popup__desc_messagebox.form__message_error.js-formError')

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
