from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from partidas.models import Match


class BetGroupManager(models.Manager):

    def create(self, *args, **kwargs):
        '''
        Cria Aposta e adiciona um 'code' com base nos seus campos 
        '''
        obj = super(BetGroupManager, self).create(*args, **kwargs)
        user = str(obj.user.pk).zfill(3) + '-' if obj.user else ''
        date = str(obj.date.day) + '/' + str(obj.date.month)
        obj.code = str(obj.pk) + '/' + user + date
        obj.save()
        return obj


class BetGroup(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    value = models.DecimalField(_('Value'), decimal_places=2, max_digits=8)
    date = models.DateTimeField(_('Date'), default=timezone.now)
    code = models.CharField(_('Code'), max_length=126, blank=True, null=True)

    objects = BetGroupManager()


class BetManager(models.Manager):

    def create(self, *args, **kwargs):
        '''
        Cria Aposta e adiciona um 'code' com base nos seus campos 
        '''
        obj = super(BetManager, self).create(*args, **kwargs)
        match = str(obj.match.pk).zfill(3)
        obj.code = str(obj.pk) + '/' + match
        obj.save()
        return obj


class Bet(models.Model):
    code = models.CharField(_('Code'), max_length=126)
    value = models.DecimalField(_('Value'), decimal_places=2, max_digits=8)
    match = models.ForeignKey(Match, verbose_name=_('Match'))
    match_type = models.CharField(_('Type'), max_length=100)
    bet_group = models.ForeignKey(BetGroup, verbose_name=_('Bet group'))

    objects = BetManager()
