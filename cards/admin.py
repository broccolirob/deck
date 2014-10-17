from django.contrib import admin
from cards.models import Card, Player, WarGame


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(WarGame)
class WarGameAdmin(admin.ModelAdmin):
    pass
