from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models


class BetSingleFieldForm(forms.ModelForm):
    bet_value = forms.DecimalField(
        label=_('Bet\'s value'), required=True,
        min_value=5, decimal_places=2
    )
    match_pk = forms.CharField(
        label=_('Match\'s pk'),
        required=False
    )
    match_type = forms.CharField(
        label=_('Match\'s type'),
        required=False
    )

    class Meta:
        model = models.Bet
        fields = ['bet_value', 'match_pk', 'match_type']

    def clean(self):
        cleaned_data = super(BetSingleFieldForm, self).clean()
        match_pk = cleaned_data.get('match_pk').split(';')
        match_type = cleaned_data.get('match_type').split(';')
        if not match_pk or not match_type:
            self.add_error('bet_value', _('No have bet to save'))
        if len(match_pk) < 2:
            self.add_error('bet_value', _('Insufficient amount of bets'))
        return cleaned_data

    def objects_dict(self):
        match_pk = self.cleaned_data.get('match_pk').split(';')
        match_type = self.cleaned_data.get('match_type').split(';')
        return {pk: type for pk, type in zip(match_pk, match_type)}
