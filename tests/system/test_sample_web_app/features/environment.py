import logging
import os
import shutil

from configobj import ConfigObj


def before_all(context):
    config_file = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg'))
    context.suite_config = ConfigObj(config_file, file_error=True)

    output_dir = os.path.abspath(context.suite_config['output']['path'])
    _create_directory(dir_path=output_dir)

    log_path = os.path.join(output_dir, context.suite_config['log']['file_name'])
    context.config.setup_logging(filename=log_path,
                                 format='%(asctime)s [%(levelname)s] - %(message)s',
                                 level=context.suite_config['log']['level'])

    logging.info('-------------------- TEST SUITE INITIALIZED --------------------\n')


def before_feature(context, feature):
    logging.info('-------------------- BEFORE FEATURE --------------------')
    logging.info('Feature: {0}'.format(feature.name))
    logging.info('---------------------------------------------------------\n')



def before_scenario(context, scenario):
    logging.info('-------------------- BEFORE SCENARIO --------------------')
    logging.info('Scenario: {0}'.format(scenario.name))
    logging.info('---------------------------------------------------------\n')

    scenario_dir_name = scenario.name.replace(' ', '_')
    context.scenario_dir = os.path.join(os.path.abspath(context.suite_config['output']['path']), scenario_dir_name)
    _create_directory(dir_path=context.scenario_dir)

    context.users = {}
    context.cleanup_tasks = []


def after_scenario(context, scenario):
    for task in context.cleanup_tasks:
        try:
            task(context)
        except Exception as e:
            logging.exception('Error executing cleanup task:\n{0}'.format(e))


def _create_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path, ignore_errors=True)
    os.makedirs(dir_path)
