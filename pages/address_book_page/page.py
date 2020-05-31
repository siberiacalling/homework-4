from framework.page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .create_group_popup import CreateGroupPopup
from .edit_group_popup import EditGroupPopup
from .ingroup_dropdown import IngroupDropdown


class AddressBookPage(BasePage):
    class Locators:
        CREATE_GROUP_LINK = (By.CSS_SELECTOR, 'a.menu__option__link.js-add-label')
        EDIT_GROUP_ICON = (By.CSS_SELECTOR,
                           '.icon.icon_right.js-edit-label.icon_folders.'
                           'icon_menu_addressbook.icon_menu_addressbook_edit')
        INGROUP_DROPDOWN_LINK = (By.XPATH, '//span[.="В группу"][@class="b-dropdown__ctrl__text"]')

        @staticmethod
        def group_container(name: str):
            return (By.XPATH, f'//span[.="{name}"][@class="menu__item__link__text menu__item__link__text_linear"]/parent::*')

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

