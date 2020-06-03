from framework.page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .create_group_popup import CreateGroupPopup
from .edit_group_popup import EditGroupPopup
from .ingroup_dropdown import IngroupDropdown
from selenium.common.exceptions import TimeoutException


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
        SUBMIT_BUTTON = (By.XPATH, '//div[@data-name="submit"]')
        REMOVE_BUTTON = (By.XPATH, '//div[@data-name="remove"]')

        CONFIRM_BUTTONS_ARRAY = (By.XPATH, '//*[contains(@class, \'btn btn_main confirm-ok\')]')
        ADD_PHONE_BUTTONS_ARRAY = (
            By.XPATH, '//div[@data-for="phones"]//a[text()=\'Добавить\' and @class="form__row__subwidget_inline '
                      'form__row__subwidget__control pseudo-link js-add-subwidget"]')
        ADD_EMAIL_BUTTONS_ARRAY = (By.XPATH,
                                   '//div[@class="form__row__subwidget form__row__subwidget_top-margin form__row__subwidget_first"]//a[text('
                                   ')=\'Добавить\']')
        PHONES_ARRAY = (By.XPATH, '//span[@class="contact__phones__item__value"]')
        EMAILS_ARRAY = (By.XPATH, '//a[@class="js-email-address"]')
        JOB_TITLE_ARRAY = (By.XPATH, '//span[@class="contact__job__item contact__job__item_job_title"]')
        BOSS_ARRAY = (By.XPATH, '//div[@class="contact__job__item contact__job__item_boss"]')
        NICK_ARRAY = (By.XPATH, '//span[@class="contact__header__title__additional"]')
        GENDERS_ARRAY = (By.XPATH, '//input[@name="sex"]')
        BUTTONS_BELLOW_ARRAY = (By.XPATH, '//span[text()=\'Добавить поле\']')
        DELETE_JOB_TITLE_ARRAY = (By.XPATH, '//div[@data-for="job_title"]//a[@title="Удалить"]')
        DELETE_BOSS_ARRAY = (By.XPATH, '//div[@data-for="boss"]//a[@title="Удалить"]')
        DELETE_NICK_ARRAY = (By.XPATH, '//div[@data-for="nick"]//a[@title="Удалить"]')

        GENDER_HEADER = (By.XPATH, '//div[@class="contact__header__additional"]')

        FIRSTNAME_EDIT_FORM = (By.NAME, 'firstname')
        LASTNAME_EDIT_FORM = (By.NAME, 'lastname')
        COMPANY_EDIT_FORM = (By.NAME, 'company')
        EMAILS_EDIT_FORM = (By.NAME, 'emails')
        FIRST_PHONE_EDIT_FORM = (By.ID, 'phones_0')

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

        @staticmethod
        def button_below_by_field_name(field_name: str):
            return (By.XPATH,
                    f'//ul[@class="form__dropdown__list form__dropdown__list_limit filters__dropdown__menu js-menu"]//a[text()=\'{field_name}\']')

    class ProjectXpath:
        @staticmethod
        def current_contact_container_in_card(lastname: str, new_firstname: str):
            return f'//*[text()=\'{lastname} {new_firstname}\']'

    def current_contact_container_in_card(self, new_firstname, lastname):
        return self.ProjectXpath.current_contact_container_in_card(lastname, new_firstname)

    def open_create_group_popup(self) -> CreateGroupPopup:
        self.wait_for_clickable(*self.Locators.CREATE_GROUP_LINK).click()
        popup = CreateGroupPopup(self.driver)
        popup.check_appear()
        return popup

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

    def click_add_button(self):
        self.wait_for_clickable(*self.Locators.ADD_BUTTON).click()

    def click_submit_button(self):
        self.wait_for_clickable(*self.Locators.SUBMIT_BUTTON).click()

    def click_remove_button(self):
        self.wait_for_clickable(*self.Locators.REMOVE_BUTTON).click()

    def add_another_field_by_input_name(self, name, new_field):
        email_input = self.wait_for_all_elements(By.NAME, name)
        email_input[-1].click()
        email_input[-1].clear()
        email_input[-1].send_keys(new_field)

    def email_was_added_successfully(self, new_email):
        contact_emails = self.wait_for_all_elements(*self.Locators.EMAILS_ARRAY)
        return contact_emails[-1].text == new_email

    def click_add_phone_button(self):
        add_buttons = self.wait_for_all_elements(*self.Locators.ADD_PHONE_BUTTONS_ARRAY)
        add_buttons[0].click()

    def click_add_email_button(self):
        add_buttons = self.wait_for_all_elements(*self.Locators.ADD_EMAIL_BUTTONS_ARRAY)
        add_buttons[0].click()

    def confirm_remove(self):
        buttons_in_list = self.wait_for_all_elements(*self.Locators.CONFIRM_BUTTONS_ARRAY)
        buttons_in_list[0].click()

    def fill_contact(self, firstname, lastname, company, email, phone):
        firstname_field = self.wait_for_visible(*self.Locators.FIRSTNAME_EDIT_FORM)
        firstname_field.clear()
        firstname_field.send_keys(firstname)

        lastname_field = self.wait_for_visible(*self.Locators.LASTNAME_EDIT_FORM)
        lastname_field.clear()
        lastname_field.send_keys(lastname)

        company_field = self.wait_for_visible(*self.Locators.COMPANY_EDIT_FORM)
        company_field.clear()
        company_field.send_keys(company)

        email_field = self.wait_for_visible(*self.Locators.EMAILS_EDIT_FORM)
        email_field.clear()
        email_field.send_keys(email)

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

    def check_element_exists_by_xpath(self, new_firstname, lastname):
        try:
            self.current_contact_container_in_card(new_firstname, lastname)
            return True
        except TimeoutException:
            return False

    def click_adressbook_href(self):
        self.wait_for_clickable(*self.Locators.ADDRESSBOOK_HREF).click()

    def click_contact_in_list(self, firstname, lastname):
        child_element = self.wait_for_visible(*self.Locators.current_contact_container_in_list(firstname, lastname))
        parent_element = child_element.find_element_by_xpath('..')
        parent_element2 = parent_element.find_element_by_xpath('..')
        parent_element2.click()

    def choose_field_button_below(self, field_name):
        add_field_buttons = self.wait_for_all_elements(*self.Locators.BUTTONS_BELLOW_ARRAY)
        parent_element = add_field_buttons[0].find_element_by_xpath('..')
        parent_element.click()
        all_buttons = self.wait_for_all_elements(*self.Locators.button_below_by_field_name(field_name))
        self.driver.execute_script("arguments[0].click();", all_buttons[1])

    def click_male_gender(self):
        genders = self.wait_for_all_elements(*self.Locators.GENDERS_ARRAY)
        self.driver.execute_script("arguments[0].click();", genders[0])

    def phone_was_added_successfully(self, new_phone):
        contact_phones = self.wait_for_all_elements(*self.Locators.PHONES_ARRAY)
        return contact_phones[-1].text == new_phone

    def job_title_was_added_successfully(self, job_title):
        value_in_contact_card = self.wait_for_all_elements(*self.Locators.JOB_TITLE_ARRAY)
        return value_in_contact_card[-1].text == job_title

    def boss_was_added_successfully(self, boss):
        value_in_contact_card = self.wait_for_all_elements(*self.Locators.BOSS_ARRAY)
        return value_in_contact_card[-1].text.split()[1] == boss

    def nick_was_added_successfully(self, nick):
        check_value = f'«{nick}»'
        value_in_contact_card = self.wait_for_all_elements(*self.Locators.NICK_ARRAY)
        return value_in_contact_card[-1].text == check_value

    def gender_was_added_successfully(self):
        contact_header = self.wait_for_visible(*self.Locators.GENDER_HEADER)
        return contact_header.text == 'Мужской'

    def click_delete_button_job_title(self):
        delete_buttons = self.wait_for_all_elements(*self.Locators.DELETE_JOB_TITLE_ARRAY)
        delete_buttons[0].click()

    def job_title_was_deleted(self):
        job_title_element = self.driver.find_elements(*self.Locators.JOB_TITLE_ARRAY)
        if not job_title_element:
            return True
        return False

    def click_delete_button_boss(self):
        delete_buttons = self.wait_for_all_elements(*self.Locators.DELETE_BOSS_ARRAY)
        delete_buttons[0].click()

    def boss_was_deleted(self):
        boss_element = self.driver.find_elements(*self.Locators.BOSS_ARRAY)
        if not boss_element:
            return True
        return False

    def click_delete_button_nick(self):
        delete_buttons = self.wait_for_all_elements(*self.Locators.DELETE_NICK_ARRAY)
        delete_buttons[0].click()

    def nick_was_deleted(self):
        nick_element = self.driver.find_elements(*self.Locators.NICK_ARRAY)
        if not nick_element:
            return True
        return False
