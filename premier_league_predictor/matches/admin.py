from django.contrib import admin
from .models import Team, Matches


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'crest',
    )


class MatchesAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'home_team',
        'home_team_score',
        'away_team',
        'away_team_score',
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(Matches, MatchesAdmin)
