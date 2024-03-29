from django.urls import path
from . import views

urlpatterns = [
  path('', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('workouts/', views.workouts_index, name='index'),
  path('workouts/<int:workout_id>/', views.workouts_detail , name='detail'),
  path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
  path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
  path('workout/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
  path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
  path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
  path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
  path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
  path('exercises/', views.ExerciseList.as_view(), name='exercises_index'),
  path('workouts/<int:workout_id>/assoc_exercise/<int:exercise_id>/', views.assoc_exercise, name='assoc_exercise'),
  path('workouts/<int:workout_id>/remove_exercise/<int:exercise_id>/', views.remove_exercise, name='remove_exercise'),
  path('workouts/<int:workout_id>/add_photo/', views.add_photo, name='add_photo'),
  path('workouts/<int:workout_id>/add_feeding', views.add_feeding, name='add_feeding'),
]