from django.contrib import admin

from . import models


@admin.register(models.Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'match', 'value', 'type')
