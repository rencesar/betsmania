from behave import step
from nose.tools import assert_true

@step(u'que acesso a página inicial')
def initial_page_access(context):
    context.browser.visit(context.base_url)


@step(u'que acesso como visitante')
def access_as_visit(context):
    assert_true(context.browser.is_text_not_present('Logado como'))
    assert_true(context.browser.is_text_present('Login'))


@step(u'clico no botão "{button}"')
def click_on_button(context, button):
    button = '//button[text()="{0}"]'.format(button)
    context.browser.find_by_xpath(button).first.click()


@step(u'clico no link "{link}"')
def click_on_button(context, link):
    context.browser.click_link_by_text(link)


@step(u'estárei na página "{message}"')
def in_page_with_message(context, message):
    print(message)
    assert_true(context.browser.is_text_present(message))

# @step(u'hoje é dia (\d{2})/(\d{2})/(\d{4})(?: às (\d{2}):(\d{2}))?')
# def set_defined_date(context, date):
#     print(context['current_date'])
#     aware = date
