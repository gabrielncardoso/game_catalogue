from django.shortcuts import render
from gamerating.models import Game

def index(request):
    context = {
            "games": Game.objects.all()
        }
    return render(request, "gamerating/index.html", context)

def detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    context = {
            "gamedetail": game
        }
    return render(request, "gamerating/detail.html", context)
