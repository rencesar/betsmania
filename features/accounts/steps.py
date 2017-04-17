from aloe import step, world
from nose.tools import assert_true, assert_false

from django.contrib.auth.models import User
from contas.factories import UserFactory


@step(r'possuo uma conta cadastrada com dados conforme abaixo')
def resgistred_user_with_args(step):
    for row in step.hashes:
        UserFactory(
            first_name=row['NOME'],
            username=row['USERNAME'],
            email=row['EMAIL'],
        )


@step(u'preencho os dados de login conforme abaixo')
def login_form(step):
    for row in step.hashes:
        world.browser.fill('username', row['USERNAME'])
        world.browser.fill('password', row['SENHA'])

@step('preencho um formulário de cadastro de usuário conforme abaixo')
def fill_user_registration_form(step):
    for row in step.hashes:
        world.browser.fill('first_name', row['NOME'])
        world.browser.fill('username', row['USERNAME'])
        world.browser.fill('email', row['EMAIL'])
        world.browser.fill('password', row['SENHA'])


@step('terei um usuário "([^"]*)" cadastrado')
def has_registered_user(step, user):
    assert_true(User.objects.filter(username=user).exists())


@step('não terei usuário chamado "([^"]*)"')
def has_no_registered_user(step, name):
    assert_false(User.objects.filter(first_name=name).exists())
