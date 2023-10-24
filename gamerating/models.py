from django.db import models

class User(models.Model):
    pass

class Game(models.Model):
    name = models.CharField(max_length=50)
    nplayers = models.CharField(max_length=5)
    genre = models.CharField(max_length=20)

class Rating(models.Model):
    score = models.SmallIntegerField(max=5, default=3)
    game = models.ForeignKey(Game)
    