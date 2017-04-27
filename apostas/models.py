from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from partidas.models import Match


class BetManager(models.Manager):

    def create(self, *args, **kwargs):
        '''
        Cria Aposta e adiciona um 'code' com base nos seus campos 
        '''
        obj = super(BetManager, self).create(*args, **kwargs)
        match = str(obj.match.pk).zfill(3)
        user = str(obj.user.pk).zfill(3) + '-' if obj.user else ''
        obj.code = str(obj.pk) + '-' + user + match
        obj.save()
        return obj


class Bet(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    code = models.CharField(_('Code'), max_length=126)
    match = models.ForeignKey(Match, verbose_name=_('Match'))
    value = models.DecimalField(_('Value'), decimal_places=2, max_digits=4)
    type = models.CharField(_('Type'), max_length=100)

    objects = BetManager()
