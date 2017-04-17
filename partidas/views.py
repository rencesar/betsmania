from django.views import generic

from . import models
from times.models import League


class MatchsListView(generic.ListView):
    model = models.Match
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(MatchsListView, self).get_context_data(**kwargs)
        context['object_list'] = {league: self.object_list.filter(league=league.pk)
                                  for league in League.objects.all()}
        return context
