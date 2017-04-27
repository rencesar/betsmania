import json
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views import generic
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from . import models, forms
from partidas.models import Match


class BetCreateView(generic.CreateView):
    form_class = forms.BetSingleFieldForm
    template_name = 'apostas/form_aposta.html'

    @cached_property
    def user(self):
        if self.request.user.is_authenticated():
            return self.request.user
        return None

    def form_invalid(self, form):
        print('oi')
        print(form)
        return self.render_to_response(self.get_context_data(form=form), status=420)

    def form_valid(self, form):
        dict_match = form.objects_dict()
        self.value = form['bet_value']
        for pk, match_type in dict_match.items():
            self.create_bet(pk, match_type)
        return self.render_to_response(self.get_context_data(form=form))

    def create_bet(self, match_pk, match_type):
        '''
        Cria aposta com dados passado pelo usuario na view
        '''
        match = Match.objects.get(pk=match_pk)
        models.Bet.objects.create(
            user=self.user, match=match,
            value=self.value*float(getattr(match, match_type)),
            type=_(type)
        )
