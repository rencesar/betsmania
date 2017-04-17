import factory

from . import models


class TeamFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Time {}'.format(n))

    class Meta:
        model = models.Team


class LeagueFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'League {}'.format(n))
    country = factory.Sequence(lambda n: 'Country {}'.format(n))

    class Meta:
        model = models.League
