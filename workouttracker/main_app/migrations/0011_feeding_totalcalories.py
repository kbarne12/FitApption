# Generated by Django 3.2.2 on 2021-05-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='totalcalories',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]