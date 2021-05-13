from django.contrib import admin
from .models import Workout, Exercise, Feeding, Photo

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Feeding)
admin.site.register(Photo)