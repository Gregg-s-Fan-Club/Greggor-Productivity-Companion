from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from greggor_productivity_companion.models import Task
from datetime import datetime, timedelta, date


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
    
    def get_remaining_points_for_current_cycle(self):
        start_date = self.date - timedelta(days=date.today().weekday())
        end_date = start_date +  timedelta(days=7)
        points = 0
        workperiods = WorkPeriod.objects.filter(task=self.task).exclude(id=self.id)
        for workperiod in workperiods:
            if workperiod.date >= start_date and workperiod.date <= end_date:
                points = points + workperiod.points
        
        max_points = self.task.category.max_points_per_cycle

        if points > max_points:
            return 0
        else:
            return max_points - points
