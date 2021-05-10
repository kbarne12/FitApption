from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User
# Create your models here.

TRAININGS = (
  ('H', 'HIIT'),
  ('C', 'cardio'),
  ('R', 'resistance')
)



class Workout(models.Model):
  date = models.DateField()
  day = models.IntegerField()
  duration = models.IntegerField()
  training = models.CharField(
    max_length=1,
    choices=TRAININGS,
    default=TRAININGS[0][0])
  calories = models.IntegerField()