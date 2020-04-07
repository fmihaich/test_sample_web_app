import time

from selenium.webdriver.common.by import By

from tests.system.test_sample_web_app.utils.page_objects.base_page import BasePage


class NewUserPage(BasePage):
    _user_input_xpath = "//input[@id='{0}']"
    _submit_btn_id = 'submit-btn'
    _all_user_input = ['username', 'name', 'surname', 'email', 'birthday', 'address']

    def insert_all_user_data(self, user_data):
        for data, value in user_data.items():
            self.insert_user_data(data, value)
        for data in [d for d in self._all_user_input if d not in user_data.keys()]:
            self.clear_user_data(data)

    def insert_user_data(self, data, value):
        user_input = self.find_element(By.XPATH, self._user_input_xpath.format(data.lower()))
        user_input.click()
        user_input.clear()
        user_input.send_keys(value)

    def clear_user_data(self, data):
        self.insert_user_data(data, value='')

    def submit_user_data(self):
        submit_btn = self.find_element(By.ID, self._submit_btn_id)
        submit_btn.click()
        time.sleep(1)
