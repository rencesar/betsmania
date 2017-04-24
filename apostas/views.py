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
    model = models.Bet
    template_name = 'apostas/form_aposta.html'

    @cached_property
    def user(self):
        if self.request.user.is_authenticated():
            return self.request.user
        return None

    def post(self, request, *args, **kwargs):
        value = request.POST.get('bet_value')
        pk_list = request.POST.getlist('match_pk')
        type_list = request.POST.getlist('match_type')
        for pk, type in zip(pk_list, type_list):
            form = self.get_form()
            form.data['bet_value'] = value
            form.data['match_pk'] = pk
            form.data['match_type'] = type
            print(form.is_valid())
        return super(BetCreateView, self).post(request, *args, **kwargs)

    def form_invalid(self, form):
        print('oi')
        print(form)
        return self.render_to_response(self.get_context_data(form=form), status=420)

    def form_valid(self, form):
        print('oi')
        print(form)
        return self.render_to_response(self.get_context_data(form=form))

    def un_used_def(self, *args, **kwargs):
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
