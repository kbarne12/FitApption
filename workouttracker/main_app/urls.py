from django.urls import path
from . import views

urlpatterns = [
  path('', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
]