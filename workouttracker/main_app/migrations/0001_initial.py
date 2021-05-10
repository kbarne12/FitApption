# Generated by Django 3.2.2 on 2021-05-10 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('training', models.CharField(choices=[('H', 'HIIT'), ('C', 'cardio'), ('R', 'resistance')], default='H', max_length=1)),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
