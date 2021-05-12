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



class Exercise(models.Model):
  name = models.CharField(max_length=100)
  reps = models.IntegerField()
  sets = models.IntegerField()
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("exercises_detail", kwargs={"pk": self.id})


class Workout(models.Model):
  date = models.DateField()
  day = models.IntegerField()
  duration = models.IntegerField()
  calories = models.IntegerField()
  weight = models.IntegerField()
  exercises = models.ManyToManyField(Exercise)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def get_absolute_url(self):
    return reverse("detail", kwargs={"workout_id": self.id})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  workouts = models.ForeignKey(Workout, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for workout_id: {self.workout_id} @{self.url}"

  
  