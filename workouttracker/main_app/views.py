from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def about(request):
  return render(request, 'about.html')

# Create your views here.
