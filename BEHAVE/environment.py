import os
import ipdb

from behave import runner
from splinter import Browser

from django.core.management import call_command
from django.utils.translation import activate


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


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    context.browser.quit()
