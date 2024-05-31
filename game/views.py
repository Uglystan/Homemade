from django.shortcuts import render
from .models import Game

def game(request):
        return render(request, 'game/game.html')

def game_rank(request):
        games = Game.objects.all().order_by('score')
        return render(request, 'game/game_rank.html', {'games' : games})
