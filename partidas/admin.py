from django.contrib import admin

from . import models


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'home_team', 'visiting_team',
                    'home_win', 'draw', 'visiting_win', 'league',
                    )
