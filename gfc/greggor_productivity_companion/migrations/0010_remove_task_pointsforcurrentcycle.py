# Generated by Django 4.2.7 on 2024-03-09 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greggor_productivity_companion', '0009_alter_workperiod_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='pointsForCurrentCycle',
        ),
    ]
