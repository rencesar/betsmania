from django.contrib import admin

from . import models


@admin.register(models.Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = (
    	'code', 'match', 'match_type',
    )


@admin.register(models.BetGroup)
class BetGroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'value','date')

