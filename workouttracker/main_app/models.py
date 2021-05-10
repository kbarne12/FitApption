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
  calories = models.IntegerField()
  weight = models.IntegerField()
  # training_type = models.CharField(
  #   max_length=1,
  #   choices=TRAININGS)
  def __str__(self):
      return self.name
  def get_absolute_url(self):
    return reverse("detail", kwargs={"workout_id": self.id})


  