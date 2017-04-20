from aloe import step, world
from datetime import datetime
from django.utils import timezone
from nose.tools import assert_equals, assert_true

from partidas.factories import MatchFactory
from times.factories import TeamFactory, LeagueFactory


@step('que existem os seguintes jogos cadastrados no sistema')
def define_games_to_challenger(step):
    for row in step.hashes:
        date = timezone.make_aware(datetime.strptime(row['DATA'], '%d/%m/%Y às %H:%M'))
        league = LeagueFactory(name=row['LIGA'])
        home = TeamFactory(name=row['TIME CASA'])
        visiting = TeamFactory(name=row['TIME FORA'])
        MatchFactory(
            home_team=home,
            visiting_team=visiting,
            date=date,
            home_win=row['CASA'],
            draw=row['EMPATE'],
            visiting_win=row['FORA'],
            league=league
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
        assert_equals(f(row, 'home_team'), data['TIME CASA'])
        assert_equals(f(row, 'visiting_team'), data['TIME FORA'])
        assert_equals(f(row, 'home_win').replace(',', '.'), data['CASA']) # TODO separar no html decimal por ponto e não por virgula
        assert_equals(f(row, 'draw').replace(',', '.'), data['EMPATE'])
        assert_equals(f(row, 'visiting_win').replace(',', '.'), data['FORA'])
