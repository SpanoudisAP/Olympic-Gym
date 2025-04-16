# Generated by Django 5.2 on 2025-04-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_remove_workout_intensity_workout_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='custom_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
