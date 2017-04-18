import pytz
from aloe import step, world
from aloe_django import django_url
from nose.tools import assert_true
from django.utils import timezone


@step(u'que acesso a página inicial')
def initial_page_access(step):
    world.browser.visit(django_url(step))


@step(u'que acesso como visitante')
def access_as_visit(step):
    assert_true(world.browser.is_text_not_present('Logado como'))
    assert_true(world.browser.is_text_present('Login'))


@step(u'clico no botão "([^"]*)"')
def click_on_button(step, button):
    button = '//button[text()="{0}"]'.format(button)
    world.browser.find_by_xpath(button).first.click()


@step(u'clico no link "([^"]*)"')
def click_on_button(step, link):
    world.browser.click_link_by_text(link)


@step(u'estárei na página "([^"]*)"')
def in_page_with_message(step, message):
    assert_true(world.browser.is_text_present(message))


@step('que hoje é dia (\d{2})/(\d{2})/(\d{4})(?: às (\d{2}):(\d{2}))?')
def set_defined_date(step, *date):
    pass
    # context.dateformat = get_datetime_django(date).astimezone(pytz.timezone('America/Recife'))


@step('hoje será dia (\d{2})/(\d{2})/(\d{4})(?: às (\d{2}):(\d{2}))?')
def set_defined_date(step, *date):
    pass

