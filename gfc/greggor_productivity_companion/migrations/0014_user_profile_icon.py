# Generated by Django 4.1.3 on 2024-03-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greggor_productivity_companion', '0013_remove_task_actual_work_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_icon',
            field=models.CharField(default='normal', max_length=30),
        ),
    ]
