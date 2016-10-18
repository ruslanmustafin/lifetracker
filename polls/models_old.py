from __future__ import unicode_literals
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=256)
    serving = models.CharField(max_length=100)
    calories = models.IntegerField()
    carb = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    fiber = models.IntegerField()


class Entry(models.Model):
    food = models.ForeignKey(Food)
    value = models.FloatField()