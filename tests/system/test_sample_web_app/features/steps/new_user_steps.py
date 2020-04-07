import logging

from behave import step
from random import randint

from tests.system.test_sample_web_app.utils.user_mgmt import get_user_from_context, DEFAULT_USER_ID


@step(u'I complete all user information for a user')
@step(u'I complete all user information for "{user_id}" user')
def complete_user_data(context, user_id=DEFAULT_USER_ID):
    user = get_user_from_context(context, user_id)
    _insert_user_data_in_the_web_page(context, user)


@step(u'I complete all user information for a user which "{user_data}" is "{data_value}"')
def complete_user_info_with_specific_data(context, user_data, data_value):
    user = get_user_from_context(context, user_id=DEFAULT_USER_ID)
    user[user_data] = data_value
    _insert_user_data_in_the_web_page(context, user)


@step(u'I complete all user information except "{missing_data}"')
def complete_user_info_without_specifying_some_data(context, missing_data):
    user = get_user_from_context(context)
    del user[missing_data]
    _insert_user_data_in_the_web_page(context, user)


@step(u'I click on submit user button')
def click_on_submit_btn(context):
    new_user_page = context.current_page
    new_user_page.submit_user_data()


@step(u'I submit "{user_count:d}" users')
def submit_multiple_users(context, user_count):
    user_id_prefix = 'user_{0}'.format(randint(0, 1000000))
    for i in range(1, user_count+1):
        user_id = user_id_prefix + '_{0}'.format(i)
        context.execute_steps(u'''
            Given I complete all user information for "{0}" user
            And I click on submit user button'''.format(user_id))


def _insert_user_data_in_the_web_page(context, user):
    new_user_page = context.current_page
    logging.info('Inserting the following user info tin the web page: "{0}"'.format(user))
    new_user_page.insert_all_user_data(user)
