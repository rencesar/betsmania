from aloe import step, world
from datetime import datetime
from django.utils import timezone
from nose.tools import assert_equals, assert_true

from partidas.factories import MatchFactory


@step('que existem os seguintes jogos cadastrados no sistema')
def define_games_to_challenger(step):
    for row in step.hashes:
        date = timezone.make_aware(datetime.strptime(row['DATA'], '%d/%m/%Y às %H:%M'))
        MatchFactory(
            home_team=row['TIME CASA'],
            visiting_team=row['TIME FORA'],
            date=date,
            home_win=row['CASA'],
            draw=row['EMPATE'],
            visiting_win=row['FORA'],
        )


def f(root, name):
    field = root.find_by_css('[data-field="%s"]' % name)
    return field.text if field else ''


@step('verei os seguintes jogos na tela')
def matchs_on_page(step):
    rows = world.browser.find_by_css('table tbody tr')
    assert_equals(len(rows), len(step.hashes))

    for row, data in zip(rows, step.hashes):
        assert_equals(f(row, 'date'), data['DATA'])
        assert_equals(f(row, 'house_team'), data['TIME CASA'])
        assert_equals(f(row, 'visiting_team'), data['TIME FORA'])
        assert_equals(f(row, 'house_win'), data['CASA'])
        assert_equals(f(row, 'draw'), data['EMPATE'])
        assert_equals(f(row, 'visiting_win'), data['FORA'])