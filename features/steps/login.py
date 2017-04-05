from behave import step
from contas.factories import UserFactory


@step(r'possuo uma conta cadastrada com dados conforme abaixo')
def resgistred_user_with_args(context):
    for row in context.table:
        UserFactory(
            first_name=row['NOME'],
            username=row['USERNAME'],
            email=row['EMAIL'],
            password=row['SENHA'],
        )


@step(u'preencho os dados de login conforme abaixo')
def login_form(context):
    for row in context.table:
        context.browser.fill('username', row['USERNAME'])
        context.browser.fill('password', row['SENHA'])