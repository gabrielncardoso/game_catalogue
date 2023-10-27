from django.db import models
from django.db.models import Avg

class User(models.Model):
    pass
    #VIEW LIST OF GAMES AND THEIR COLUMNS
    #ONLY CAN VIEW THE AVERAGE RATING OF EACH GAME
    #GIVE A SCORE TO A GAME

class Game(models.Model):
    name = models.CharField(max_length=50)
    nplayers = models.CharField(max_length=5)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.name}')
    
    def avgscore(self):
        avg = self.rating_set.aggregate(Avg("score"))
        return "%.2f" % avg["score__avg"]

class Rating(models.Model):
    score = models.SmallIntegerField(default=3)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    def __str__(self):
        return (f'{self.score}, {self.game.name}')
