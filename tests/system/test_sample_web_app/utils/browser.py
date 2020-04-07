import os
from selenium import webdriver


class Browser(object):

    def __init__(self):
        command_executor = 'http://' + os.environ['WEBDRIVER_HOST'] + ':4444/wd/hub'
        self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME,
                                       command_executor=command_executor)
        self.driver.implicitly_wait(2)

    def close(self):
        self.driver.close()

    def go_to(self, url):
        self.driver.get(url)
        return self.driver

    def refresh(self):
        self.driver.refresh()
