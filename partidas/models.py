from django.db import models
from django.utils.translation import ugettext_lazy as _

from times.models import Team, League


class Match(models.Model):
    home_team = models.ForeignKey(Team, verbose_name=_('Home team'),
                                  related_name='home_team')
    visiting_team = models.ForeignKey(Team, verbose_name=_('Visiting team'),
                                      related_name='visiting_team')
    date = models.DateTimeField(_('Match date'))
    home_win = models.DecimalField(_('Home team win'), decimal_places=2, max_digits=3)
    draw = models.DecimalField(_('Draw'), decimal_places=2, max_digits=3)
    visiting_win = models.DecimalField(_('Visiting team win'), decimal_places=2, max_digits=3)
    league = models.ForeignKey(League, verbose_name=_('League'))
