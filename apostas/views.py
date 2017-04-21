import json
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from . import models
from partidas.models import Match


class BetCreateView(generic.View):
    model = models.Bet

    @cached_property
    def user(self):
        if self.request.user.is_authenticated():
            return self.request.user
        return None

    @cached_property
    def value(self):
        value = self.request.GET.get('betsvalue', None)
        if value is None:
            return value
        return float(value.replace(',', '.'))

    def get(self, *args, **kwargs):
        if not self.value:
            messages.info(self.request, _('Bet\'s value not defined'))
            return HttpResponse(self.request)
        data = json.loads(self.request.GET['data'])
        for key in data:
            self.create_bet(Match.objects.get(pk=key), data[key])
        return HttpResponse(json.dumps({'success': False, 'message': 'passou'}), content_type='application/json')

    def create_bet(self, match, type):
        '''
        Cria aposta com dados passado pelo usuario na view
        '''
        self.model.objects.create(
            user=self.user, match=match,
            value=self.value*float(getattr(match, type)),
            type=_(type)
        )
