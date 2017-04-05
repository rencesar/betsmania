from behave import step


@step(u'que acesso a página inicial')
def initial_page_access(context):
    context.browser.visit(context.server_url)


@step(u'que acesso como visitante')
def access_as_visit(context):
    context.browser.is_text_not_present('Logado como')
    context.browser.is_text_present('Login')


@step(u'clico no botão "{button}"')
def click_on_button(context, button):
    button = '//button[text()="{0}"]'.format(button)
    context.browser.find_by_xpath(button).first.click()


@step(u'clico no link "{link}"')
def click_on_button(context, link):
    context.browser.click_link_by_text(link)


@step(u'estárei na pagina "{message}"')
def in_page_with_message(context, message):
    assert context.browser.is_text_present(message)
