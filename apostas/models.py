from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from partidas.models import Match


class BetManager(models.Manager):
    def create_with_code(self, *args, **kwargs):
        obj = self.create(*args, **kwargs)
        user = str(obj.user.pk).zfill(4)
        match = str(obj.match.pk).zfill(6)
        value = str(obj.value).replace('.', '').zfill(4)
        obj.code = user + match + value
        obj.save()


class Bet(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    code = models.CharField(_('Code'), max_length=126)
    match = models.ForeignKey(Match, verbose_name=_('Match'))
    value = models.DecimalField(_('Value'), decimal_places=2, max_digits=4)
    type = models.CharField(_('Type'), max_length=100)

    objects = BetManager()
