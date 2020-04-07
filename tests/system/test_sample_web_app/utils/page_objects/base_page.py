import logging


TRANSLATE_TO_UPPER = "translate({0}, 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator, retries=4):
        for _ in range(retries+1):
            try:
                return self.driver.find_element(by, locator)
            except:
                logging.warning('Unable to find "{0}" web element by "{1}"'.format(locator, by))
        raise Exception('Unable to find "{0}" web element by "{1}"'.format(locator, by))

    def find_elements(self, by, locator, retries=4):
        for _ in range(retries+1):
            try:
                return self.driver.find_elements(by, locator)
            except:
                logging.warning('Unable to find "{0}" web elements by "{1}"'.format(locator, by))
        raise Exception('Unable to find "{0}" web elements by "{1}"'.format(locator, by))
