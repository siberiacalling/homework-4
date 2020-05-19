from framework.page import BasePage
from selenium.webdriver.common.by import By


class AuthPage(BasePage):
    class Locators:
        LOGIN_FORM_CONTAINER = (By.CSS_SELECTOR, '.ag-popup__frame__layout__iframe')
        LOGIN_FORM = (By.CSS_SELECTOR, 'input[name="Login"]')
        TO_PASSWORD_BTN = (By.CSS_SELECTOR, 'button[data-test-id="next-button"]')
        PASSWORD_FORM = (By.CSS_SELECTOR, 'input[name="Password"]')
        SUBMIT_BTN = (By.CSS_SELECTOR, 'button[data-test-id="submit-button"]')
        EMAIL_LABEL = (By.ID, 'PH_user-email')

    def wait_for_form(self):
        iframe = self.wait_for_visible(*self.Locators.LOGIN_FORM_CONTAINER)
        self.driver.switch_to.frame(iframe)

    def fill_login_form(self, login: str):
        login_form = self.wait_for_clickable(*self.Locators.LOGIN_FORM)
        login_form.click()
        login_form.send_keys(login)

    def switch_to_password(self):
        to_password_btn = self.wait_for_clickable(*self.Locators.TO_PASSWORD_BTN)
        to_password_btn.click()

    def fill_password_form(self, password: str):
        password_form = self.wait_for_clickable(*self.Locators.PASSWORD_FORM)
        password_form.click()
        password_form.send_keys(password)

    def submit(self):
        submit_btn = self.wait_for_clickable(*self.Locators.SUBMIT_BTN)
        submit_btn.click()

    def wait_for_logged_in(self, login: str):
        self.driver.switch_to.default_content()
        logout_link = self.wait_for_clickable(*self.Locators.EMAIL_LABEL)
        assert logout_link.text == login
