import logging
import time
import os

from behave import step

from tests.system.test_sample_web_app.utils.page_objects.web_app_page import WebAppPage
from tests.system.test_sample_web_app.utils.browser import Browser


@step(u'The web app is opened')
def open_web_app(context):
    context.browser = Browser()
    context.cleanup_tasks.append(close_browser)

    web_app_url = 'http://{host}:{port}'.format(host=os.environ['WEBAPP_HOST'], port=os.environ['WEBAPP_PORT'])
    logging.info('Web app url: "{0}"'.format(web_app_url))
    context.browser.go_to(url=web_app_url)
    time.sleep(2)

    context.current_page = WebAppPage(context.browser.driver)


@step(u'I click on "{menu_option}" option')
def click_on_menu_option(context, menu_option):
    web_app_page = context.current_page
    web_app_page.select_menu_option(menu_option)


def close_browser(context):
    if hasattr(context, 'browser'):
        try:
            context.browser.close()
        except Exception as e:
            logging.warning('Error closing the browser: "{0}"'.format(e))
