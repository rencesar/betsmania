from behave import step
from apostador.factories import UserFactory


@step(r'possuo uma conta cadastrada com dados conforme abaixo')
def resgistred_user_with_args(context):
    for row in context.table:
        UserFactory(
            first_name=row['NOME'],
            username=row['USERNAME'],
            email=row['EMAIL'],
            password=row['SENHA'],
        )


@step(u'que acesso como visitante')
def access_as_visit(context):
    pass


@step(u'que está na página inicial')
def initial_page_access(context):
    erro


@step(u'clico no botão "Login"')
def click_on_button(context):
    pass


@step(u'estárei na pagina "{message}"')
def in_page_with_message(context, message):
    print('MEU NOME Não é JHON')
    pass


@step(u'preencho os dados conforme abaixo')
def populated_form(context):
    pass
