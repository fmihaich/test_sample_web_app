from selenium.webdriver.common.by import By

from tests.system.test_sample_web_app.utils.page_objects.base_page import BasePage, TRANSLATE_TO_UPPER


class AllUsersPage(BasePage):
    _table_elements_xpath = "//table[@class='table small']/tbody/tr"
    _table_headers_xpath = "//table[@class='table small']/thead/tr/th"

    def get_all_users(self):
        table_headers = self.find_elements(By.XPATH, self._table_headers_xpath)
        table_rows = self.find_elements(By.XPATH, self._table_elements_xpath)

        users = []
        for row in range(1, len(table_rows) + 1):
            row_elements = self.find_elements(By.XPATH, self._table_elements_xpath + '[{0}]/td'.format(row))
            users.append(dict(zip(map(lambda x: str(x.text.strip().lower()), table_headers),
                                  map(lambda x: str(x.text.strip()), row_elements))))

        return users
