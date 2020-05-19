from framework.test import BaseTest
from steps.auth_steps import AuthSteps
import os


class AuthTest(BaseTest):
    def test_auth(self):
        steps = AuthSteps(self.driver)
        steps.open_url('https://e.mail.ru/login?page=https%3a%2f%2fe.mail.ru%2faddressbook')
        steps.wait_for_form()
        steps.login(login=os.environ.get('LOGIN'), password=os.environ.get('PASSWORD'))
