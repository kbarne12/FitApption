from django.urls import path
from . import views

urlpatterns = [
  path('', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('workouts/', views.workouts_index, name='index'),
  path('workouts/<int:workout_id>/', views.workouts_detail , name='detail'),
]