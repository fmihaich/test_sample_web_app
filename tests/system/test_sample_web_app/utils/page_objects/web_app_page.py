import time

from selenium.webdriver.common.by import By

from tests.system.test_sample_web_app.utils.page_objects.all_users_page import AllUsersPage
from tests.system.test_sample_web_app.utils.page_objects.base_page import BasePage, TRANSLATE_TO_UPPER
from tests.system.test_sample_web_app.utils.page_objects.new_user_page import NewUserPage


class MenuOption(object):
    HOME = 'HOME'
    NEW_USER = 'NEW USER'
    ALL_USERS = 'ALL USERS'

    def get_all(self):
        return [self.HOME, self.NEW_USER, self.ALL_USERS]


MENU_XPATH = 'menu_xpath'
MENU_PAGE = 'menu_return_page'


class WebAppPage(BasePage):
    _menu_xpath = "//div[@id='myNavbar']//li[contains(" + TRANSLATE_TO_UPPER.format('.') + ", '{0}')]"
    _feedback_main_message_xpath = "//div[contains(@class, 'alert alert-dismissible')]/strong"

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._menu = {
            MenuOption.HOME: {
                MENU_XPATH: self._menu_xpath.format(MenuOption.HOME),
                MENU_PAGE: self
            },
            MenuOption.NEW_USER: {
                MENU_XPATH: self._menu_xpath.format(MenuOption.NEW_USER),
                MENU_PAGE: NewUserPage(driver)
            },
            MenuOption.ALL_USERS: {
                MENU_XPATH: self._menu_xpath.format(MenuOption.ALL_USERS),
                MENU_PAGE: AllUsersPage(driver)
            }
        }
        self._current_menu_page = self

    def select_menu_option(self, menu_option):
        menu_option = menu_option.upper()
        if menu_option not in self._menu:
            raise NotImplementedError('Option "{0}" is not available: "{1}"'.format(menu_option, self._menu.keys()))

        option = self.find_element(By.XPATH, self._menu[menu_option][MENU_XPATH])
        option.click()
        time.sleep(2)

        self._current_menu_page = self._menu[menu_option][MENU_PAGE]

    def get_feedback_message(self):
        feedback_message = self.find_element(By.XPATH, self._feedback_main_message_xpath)
        return feedback_message.text.strip()

    # The following code allow the execution of a menu option functionality
    def __getattr__(self, method_name):
        def execute_current_menu_method(*args):
            current_menu_method = getattr(self._current_menu_page, method_name)
            return current_menu_method(*args)
        return execute_current_menu_method
