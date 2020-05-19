from framework.steps import BaseSteps
from pages.auth_page import AuthPage
import os


class AuthSteps(BaseSteps):
    page: AuthPage

    def __init__(self, driver):
        super().__init__(AuthPage(driver))

    def auth(self):
        self.open_url('https://e.mail.ru/login?page=https%3a%2f%2fe.mail.ru%2faddressbook')
        self.wait_for_form()
        self.login(login=os.environ.get('LOGIN'), password=os.environ.get('PASSWORD'))

    def wait_for_form(self):
        self.page.wait_for_form()

    def login(self, login: str, password: str):
        self.page.fill_login_form(login)
        self.page.switch_to_password()
        self.page.fill_password_form(password)
        self.page.submit()
        self.page.wait_for_logged_in(login)
