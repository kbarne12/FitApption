# Generated by Django 3.2.2 on 2021-05-13 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_workouts_photo_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField(verbose_name='Calories')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.workout')),
            ],
        ),
    ]
