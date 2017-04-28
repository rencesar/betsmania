from django.contrib import admin

from . import models


@admin.register(models.BetGroup)
class BetGroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'value','date')
    search_fields = [
        'user__first_name', 'user__username', 'code',
    ]
            

class BetAdmin(admin.ModelAdmin):
    list_display = [
        'code', 'user', 'match', 'match_type', 'date'
    ]
    list_filter = ('code', 'bet_group__user', 'bet_group__date')
    search_fields = [
        'bet_group__user__first_name', 'bet_group__user__username',
        'code', 'bet_group__code'
    ]

    def user(self, obj):
        if obj.bet_group.user:
            return obj.bet_group.user.first_name
        return 'Visitante'

    def date(self, obj):
        return obj.bet_group.date


admin.site.register(models.Bet, BetAdmin)
