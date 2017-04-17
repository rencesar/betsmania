import factory

from . import models
from times.factories import TeamFactory


class MatchFactory(factory.DjangoModelFactory):
    home_team = factory.SubFactory(TeamFactory)
    visiting_team = factory.SubFactory(TeamFactory)

    class Meta:
        model = models.Match
