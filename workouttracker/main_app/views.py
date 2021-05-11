from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Exercise

# Define the home view
def about(request):
  return render(request, 'about.html')
@login_required

def workouts_index(request):
  workouts = Workout.objects.filter()
  return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  workout_exercise = Exercise.objects.exclude(id_in = workout.exercies.all().value_list('id'))
  return render(request, 'workouts/detail.html', {'workout': workout}, {'exercises' : workout_exercise})

class WorkoutCreate(CreateView):
  model = Workout
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WorkoutUpdate(UpdateView):
  model = Workout
  fields = ['date', 'day', 'calories', 'weight', 'duration']

class WorkoutDelete(DeleteView):
  model = Workout
  success_url = '/workouts/'

class ExerciseList(ListView):
  model = Exercise


class ExerciseDetail(LoginRequiredMixin, DetailView):
  model = Exercise

class ExerciseCreate(CreateView):
  model = Exercise
  fields = '__all__'

class ExerciseUpdate(UpdateView):
  model = Exercise
  fields = '__all__'

class ExerciseDelete(DeleteView):
  model = Exercise
  success_url = '/exercises/'






def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


