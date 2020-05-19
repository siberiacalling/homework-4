from framework.page import BasePage
from selenium.webdriver.common.by import By


class EditGroupPopup(BasePage):
    class Locators:
        CONTAINER = (By.CSS_SELECTOR, '.popup.js-layer.popup_dark.popup_')
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
