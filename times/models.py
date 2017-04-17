from django.db import models
from django.utils.translation import ugettext_lazy as _


class League(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    country = models.CharField(_('Country'), max_length=126)
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    stadium = models.CharField(_('Stadium'), max_length=254, blank=True)
    leagues = models.ManyToManyField(League, verbose_name=_('League'), blank=True)
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        return self.name
