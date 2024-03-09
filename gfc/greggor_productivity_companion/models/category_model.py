from django.db import models
from greggor_productivity_companion.models import Task
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Category model used for different productivity categories"""
    name: models.CharField = models.CharField(max_length=520)
    max_points_per_cycle: models.IntegerField = models.IntegerField(validators=[
            MinValueValidator(0)
        ])
    task: models.ForeignKey = models.ForeignKey(Task, on_delete=models.CASCADE)
    

