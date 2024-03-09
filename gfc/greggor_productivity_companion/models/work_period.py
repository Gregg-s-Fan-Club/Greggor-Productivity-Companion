from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from greggor_productivity_companion.models import Task
from datetime import datetime, timedelta


class WorkPeriod(models.Model):
    """Work Period model for period user spends on task"""

    date = models.DateField(blank=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False) 
    end_time = models.TimeField(auto_now=False, auto_now_add=False) 
    points = models.IntegerField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['date', 'task', 'start_time', 'end_time']

    def get_time_spent(self):
        start_timedelta  = timedelta(hours=self.start_time.hour, minutes=self.start_time.minute, seconds=self.start_time.second)
        end_timedelta  = timedelta(hours=self.end_time.hour, minutes=self.end_time.minute, seconds=self.end_time.second)
        return end_timedelta - start_timedelta

    def get_hours_spent(self):
        time_difference = self.get_time_spent()
        seconds_difference = time_difference.total_seconds()
        minutes_difference = seconds_difference / 60
        hours_difference = minutes_difference / 60
        return hours_difference
    
    
        
        

