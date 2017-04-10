import os
import pdb
# import mock
from behave import runner
from django.core.management import call_command
from django.utils.translation import activate
from splinter import Browser


os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

BEHAVE_DEBUG_ON_ERROR = False
CONTEXT = None

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("pdb")

def screenshot():
    os.system('display %s' % CONTEXT.browser.screenshot())

def before_all(context):
    activate('pt-br')
    setup_debug_on_error(context.config.userdata)
    if context.config.userdata.get('chrome', False):
        context.browser = Browser('chrome')
    else:
        context.browser = Browser('phantomjs')
        context.browser.driver.set_window_size(1024, 768)
    global CONTEXT
    CONTEXT = context
    runner.sshot = screenshot
    context.server_url = 'http://localhost:8000'


# def before_scenario(context, scenario):
#     call_command('flush', interactive=False, verbosity=0)


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        pdb.post_mortem(step.exc_traceback)
    # current_date = context.get('current_date', None)
    # if current_date:
    #     with mock.patch('django.utils.timezone.now', lambda: current_date):
    #         yield
    # else:
    #     yield


def after_all(context):
    context.browser.quit()
