import os
import mock

from aloe import world, before, around, after
from contextlib import contextmanager
from django.core.management import call_command
from django.utils.translation import activate
from splinter import Browser


def take_screenshot():
    os.system('display %s' % world.browser.screenshot())

@before.all
def before_all():
    activate('pt-br')
    chrome = os.environ.get('DRV', False)
    if chrome:
        world.browser = Browser('chrome')
    else:
        world.browser = Browser('phantomjs')
        world.browser.driver.set_window_size(1024, 768)
    world.screen = take_screenshot


@before.each_example
def create_context_and_settings_backup(scenario, *args):
    world.settings_backup = {}
    world.context = scenario.context = {}
    call_command('flush', interactive=False, verbosity=0)


@after.all
def teardown_browser():
    world.browser.quit()


@before.each_step
def set_context_at_step(step):
    step.context = world.context


@around.each_step
@contextmanager
def make_hashes_editable(step):
    step._hashes = step.hashes
    step.hashes = list(step.hashes)
    yield
    step.hashes = step._hashes


@around.each_step
@contextmanager
def use_current_date(scenario, *args):
    """
    Patch the whole step to use the current date if defined before.
    """
    current_date = world.context.get('current_date', None)
    if current_date:
        with mock.patch('django.utils.timezone.now', lambda: current_date):
            yield
    else:
        yield
