# Generated by Django 5.2 on 2025-04-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_remove_workout_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workout',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
