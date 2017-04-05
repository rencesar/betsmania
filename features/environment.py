import os
from behave import runner
from django.core.management import call_command
from django.utils.translation import activate
from splinter import Browser


os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("pdb")


def before_all(context):
    activate('pt-br')
    setup_debug_on_error(context.config.userdata)
    if context.config.userdata.get('chrome', False):
        context.browser = Browser('chrome')
    else:
        context.browser = Browser('phantomjs')
    runner.sshot = context.browser.screenshot()
    context.server_url = 'http://localhost:8000'


# def before_scenario(context, scenario):
#     call_command('flush', interactive=False, verbosity=0)


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    context.browser.quit()
