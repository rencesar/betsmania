from django.contrib import admin

from . import models


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'stadium', 'description')


@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')
