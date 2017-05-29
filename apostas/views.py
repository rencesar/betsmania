from django.contrib import messages
from django.http import HttpResponseRedirect
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
        return self.render_to_response(
            self.get_context_data(form=form), status=420
        )

    def form_valid(self, form):
        dict_match = form.objects_dict()
        self.value = float(form.cleaned_data['bet_value'])
        group = self.create_bet_group()
        print(group)
        for pk, match_type in dict_match.items():
            self.create_bet(pk, match_type, group)
        messages.success(
            self.request, _('Your bet has been successfully placed')
        )
        return self.render_to_response(self.get_context_data())

    def create_bet_group(self):
        return models.BetGroup.objects.create(
            user=self.user, value=self.value
        )

    def create_bet(self, match_pk, match_type, group):
        '''
        Cria aposta com dados passado pelo usuario na view
        '''
        match = Match.objects.get(pk=match_pk)
        models.Bet.objects.create(
            match=match,
            value=float(getattr(match, match_type)),
            match_type=_(match_type), bet_group=group
        )


class UserBetListView(generic.ListView):
    model = models.BetGroup
    template_name = 'apostas/usuarioApostas.html'

    @cached_property
    def user(self):
        return self.request.user

    def get_queryset(self):
        queryset = super(UserBetListView, self).get_queryset()
        queryset.filter(user=self.user)
        return queryset


class UserBetDeleteView(generic.DeleteView):
    model = models.BetGroup

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.paid or len(self.object.bet) < 3:
            messages.error(request, _('You already paid out this bet'))
        else:
            self.object.delete()
            messages.success(request, _('Your bet was deleted successfully!'))
        return HttpResponseRedirect('apostas:minhas-apostas')
