from .component import Component
from .page import Page


class AuthPage(Page):
    @property
    def get_form_component(self):
        return FormComponent(self.driver, 'div #mailbox-container')


class FormComponent(Component):
    def input_login(self, email):
        elem = self.container.find_element_by_id('mailbox:login')
        elem.click()
        elem.clear()
        elem.send_keys(email)

    def input_password(self, password):
        elem = self.container.find_element_by_id('mailbox:password')
        elem.click()
        elem.clear()
        elem.send_keys(password)

    def submit_login(self):
        self.container.find_element_by_xpath('//input[@class="o-control"][@value="Ввести пароль"]').click()

    def submit_password(self):
        self.container.find_element_by_xpath('//input[@class="o-control"][@value="Ввести пароль"]').click()

    def authenticate(self, email, password):
        self.input_login(email)
        self.submit_login()

        self.input_password(password)
        self.submit_password()
