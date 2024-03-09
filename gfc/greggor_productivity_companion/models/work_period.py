from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class WorkPeriod(AbstractUser):
    """Work Period model for period user spends on task"""

    date = models.DateField((unique=True, blank=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False) 
    end_time = models.TimeField(auto_now=False, auto_now_add=False) 
    points = models.IntegerField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)