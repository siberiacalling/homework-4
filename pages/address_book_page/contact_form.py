from framework.page import BasePage
from selenium.webdriver.common.by import By


class ContactForm(BasePage):
    class Locators:
        BUTTONS_BELLOW_ARRAY = (By.XPATH, '//span[text()=\'Добавить поле\']')

        DELETE_JOB_TITLE_ARRAY = (By.XPATH, '//div[@data-for="job_title"]//a[@title="Удалить"]')
        DELETE_BOSS_ARRAY = (By.XPATH, '//div[@data-for="boss"]//a[@title="Удалить"]')
        DELETE_NICK_ARRAY = (By.XPATH, '//div[@data-for="nick"]//a[@title="Удалить"]')

        GENDERS_ARRAY = (By.XPATH, '//input[@name="sex"]')
        ADD_PHONE_BUTTONS_ARRAY = (
            By.XPATH, '//div[@data-for="phones"]//a[text()=\'Добавить\' and @class="form__row__subwidget_inline '
                      'form__row__subwidget__control pseudo-link js-add-subwidget"]')
        ADD_EMAIL_BUTTONS_ARRAY = (By.XPATH,
                                   '//div[@class="form__row__subwidget form__row__subwidget_top-margin form__row__subwidget_first"]//a[text('
                                   ')=\'Добавить\']')

        FIRSTNAME_EDIT_FORM = (By.NAME, 'firstname')
        LASTNAME_EDIT_FORM = (By.NAME, 'lastname')
        COMPANY_EDIT_FORM = (By.NAME, 'company')
        EMAILS_EDIT_FORM = (By.NAME, 'emails')
        FIRST_PHONE_EDIT_FORM = (By.ID, 'phones_0')

        SUBMIT_BUTTON = (By.XPATH, '//div[@data-name="submit"]')

        @staticmethod
        def button_below_by_field_name(field_name: str):
            return (By.XPATH,
                    f'//ul[@class="form__dropdown__list form__dropdown__list_limit filters__dropdown__menu js-menu"]//a[text()=\'{field_name}\']')

    def choose_field_button_below(self, field_name):
        add_field_buttons = self.wait_for_all_elements(*self.Locators.BUTTONS_BELLOW_ARRAY)
        parent_element = add_field_buttons[0].find_element_by_xpath('..')
        parent_element.click()
        all_buttons = self.wait_for_all_elements(*self.Locators.button_below_by_field_name(field_name))
        # all_buttons[1].click()
        self.driver.execute_script("arguments[0].click();", all_buttons[1])

    def add_another_field_by_input_name(self, name, new_field):
        email_input = self.wait_for_all_elements(By.NAME, name)
        email_input[-1].click()
        email_input[-1].clear()
        email_input[-1].send_keys(new_field)

    def click_submit_button(self):
        self.wait_for_clickable(*self.Locators.SUBMIT_BUTTON).click()

    def click_delete_button_job_title(self):
        delete_buttons = self.wait_for_all_elements(*self.Locators.DELETE_JOB_TITLE_ARRAY)
        delete_buttons[0].click()

    def click_delete_button_boss(self):
        delete_buttons = self.wait_for_all_elements(*self.Locators.DELETE_BOSS_ARRAY)
        delete_buttons[0].click()

    def click_delete_button_nick(self):
        delete_buttons = self.wait_for_all_elements(*self.Locators.DELETE_NICK_ARRAY)
        delete_buttons[0].click()

    def fill_contact(self, firstname, lastname, company, email, phone):
        if firstname:
            firstname_field = self.wait_for_visible(*self.Locators.FIRSTNAME_EDIT_FORM)
            firstname_field.clear()
            firstname_field.send_keys(firstname)
        if lastname:
            lastname_field = self.wait_for_visible(*self.Locators.LASTNAME_EDIT_FORM)
            lastname_field.clear()
            lastname_field.send_keys(lastname)
        if company:
            company_field = self.wait_for_visible(*self.Locators.COMPANY_EDIT_FORM)
            company_field.clear()
            company_field.send_keys(company)
        if email:
            email_field = self.wait_for_visible(*self.Locators.EMAILS_EDIT_FORM)
            email_field.clear()
            email_field.send_keys(email)
        if phone:
            phone_field = self.wait_for_visible(*self.Locators.FIRST_PHONE_EDIT_FORM)
            phone_field.clear()
            phone_field.send_keys(phone)

    def change_email(self, new_email):
        email_field = self.wait_for_visible(*self.Locators.EMAILS_EDIT_FORM)
        email_field.clear()
        email_field.send_keys(new_email)

    def change_firstname(self, new_firstname):
        firstname_field = self.wait_for_visible(*self.Locators.FIRSTNAME_EDIT_FORM)
        firstname_field.click()
        firstname_field.clear()
        firstname_field.send_keys(new_firstname)

    def click_add_phone_button(self):
        add_buttons = self.wait_for_all_elements(*self.Locators.ADD_PHONE_BUTTONS_ARRAY)
        add_buttons[0].click()

    def click_add_email_button(self):
        add_buttons = self.wait_for_all_elements(*self.Locators.ADD_EMAIL_BUTTONS_ARRAY)
        add_buttons[0].click()

    def click_male_gender(self):
        genders = self.wait_for_all_elements(*self.Locators.GENDERS_ARRAY)
        genders[0].click()
        # self.driver.execute_script("arguments[0].click();", genders[0])
