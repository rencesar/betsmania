from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models


class BetSingleFieldForm(forms.ModelForm):
    bet_value = forms.DecimalField(
        label=_('Bet\'s value'), required=True,
        min_value=5, decimal_places=2
    )
    match_pk = forms.IntegerField(
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

    def clean_match_type(self):
        match_type = self.cleaned_data.get('match_type')
        print(self.cleaned_data)
        if not match_type:
            raise forms.ValidationError(_('No have bet to save'))
        return match_type

    def clean_match_pk(self):
        match_type = self.cleaned_data['match_pk']
        if not match_type:
            raise forms.ValidationError(_('No have bet to save'))
        return match_type
    #
    # def clean(self):
    #     cleaned_data = super(BetSingleFieldForm, self).clean()
    #     match_pk = cleaned_data.get('match_pk')
    #     match_type = cleaned_data.get('match_type')
    #     if not match_pk and not match_type:
    #         self.add_error('bet_value', _('No have bet to save'))
