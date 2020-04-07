import logging

from behave import step
from hamcrest import assert_that, has_item, not_

from tests.system.test_sample_web_app.utils.user_mgmt import get_user_from_context, DEFAULT_USER_ID


@step(u'The recent submitted user is shown')
def check_user_is_shown(context):
    _check_multiple_users_are_shown(context, user_ids=[DEFAULT_USER_ID])


@step(u'All the users are shown')
def check_all_users_are_shown(context):
    _check_multiple_users_are_shown(context, user_ids=context.users.keys())


@step(u'The user is not shown')
def check_user_is_not_shown(context):
    shown_users = _get_all_shown_users(context)
    expected_user = get_user_from_context(context)
    logging.info('Expected user to be not shown: "{0}"'.format(expected_user))
    assert_that(shown_users, not_(has_item(expected_user)))


def _check_multiple_users_are_shown(context, user_ids):
    shown_users = _get_all_shown_users(context)
    for user_id in user_ids:
        expected_user = get_user_from_context(context, user_id)
        logging.info('Expected user: "{0}"'.format(expected_user))
        assert_that(shown_users, has_item(expected_user))


def _get_all_shown_users(context):
    all_users_page = context.current_page
    shown_users = all_users_page.get_all_users()
    logging.info('Shown users: "{0}"'.format(shown_users))
    return shown_users
