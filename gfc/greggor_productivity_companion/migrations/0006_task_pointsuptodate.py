# Generated by Django 4.2.7 on 2024-03-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greggor_productivity_companion', '0005_alter_task_name_alter_task_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pointsUpToDate',
            field=models.IntegerField(default=0),
        ),
    ]