from django.db import models
from greggor_productivity_companion.models import User, Category

class Task(models.Model):
    """Task model used for different productivity tasks"""
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=520)
    description: models.CharField = models.CharField(max_length=520)
    expected_work_time: models.DurationField = models.DurationField()
    actual_work_time: models.DurationField = models.DurationField()
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)
    completed: models.BooleanField = models.BooleanField()
    

