from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from greggor_productivity_companion.models import Task
from datetime import datetime


class WorkPeriod(models.Model):
    """Work Period model for period user spends on task"""

    date = models.DateField(blank=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False) 
    end_time = models.TimeField(auto_now=False, auto_now_add=False) 
    points = models.IntegerField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['date', 'task', 'start_time', 'end_time']

    def get_hours_spent(self):
        t1 = datetime.strptime(self.start_time, "%H:%M:%S")
        t2 = datetime.strptime(self.end_time, "%H:%M:%S")
        difference = t2 - t1
        seconds_difference = difference.total_seconds()
        minutes_difference = seconds_difference / 60
        hours_difference = minutes_difference / 60
        return hours_difference
    
    
        
        

