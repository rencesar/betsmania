from behave import step
from nose.tools import assert_true, assert_false

from django.contrib.auth.models import User


@step('preencho um formulário de cadastro de usuário conforme abaixo')
def fill_user_registration_form(context):
    for row in context.table:
        context.browser.fill('first_name', row['NOME'])
        context.browser.fill('username', row['USERNAME'])
        context.browser.fill('email', row['EMAIL'])
        context.browser.fill('password', row['SENHA'])


@step('terei um usuário "{user}" cadastrado')
def has_registered_user(context, user):
    assert_true(User.objects.filter(username=user).exists())


@step('não terei usuário chamado "{name}"')
def has_no_registered_user(context, name):
    assert_false(User.objects.filter(first_name=name).exists())
