import logging

from behave import step
from hamcrest import assert_that, is_in


@step(u'I see a "{expected_feedback}" feedback message')
def check_input_feedback(context, expected_feedback):
    web_app_page = context.current_page
    current_feedback = web_app_page.get_feedback_message()
    logging.info('Current feedback: {0}'.format(current_feedback))
    assert_that(expected_feedback.lower(), is_in(current_feedback.lower()))
