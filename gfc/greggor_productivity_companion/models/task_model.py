from django.db import models
from greggor_productivity_companion.models import User, Category
from greggor_productivity_companion import models as gpcmodels
from datetime import datetime, timedelta


class Task(models.Model):
    """Task model used for different productivity tasks"""
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=520, blank=False)
    description: models.CharField = models.CharField(max_length=520)
    expected_work_time: models.DurationField = models.DurationField(blank=False)
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)
    completed: models.BooleanField = models.BooleanField(default=False)
    bonus_points = models.IntegerField(blank=False, default=0)
    
    def get_user_tasks_for_category(self) -> list:
            """Return list of the users transactions"""
            tasks: list[fcmodels.Tasks] = fcmodels.Task.objects.filter(
                user=self, category=filter_type)

            return tasks


    def get_task_workflows(self):
        return gpcmodels.WorkPeriod.objects.filter(task = self)
    
    def get_latest_task_workflow(self):
        return self.get_task_workflows().order_by('-date', '-end_time', '-start_time')[0]
    
    def get_task_workflows_over_period(self, amount):
        time = datetime.today() - timedelta(days=amount)
        return gpcmodels.WorkPeriod.objects.filter(date__gte=time, task = self)
    
    def get_task_points(self):
        work_periods = self.get_task_workflows()
        points = 0
        for period in work_periods:
            points += period.points
        return points

    def get_actual_work_time(self):
        work_periods = self.get_task_workflows()
        if len(work_periods) == 0:
             return "00:00:00"
        
        work_time = timedelta()
        for work_period in work_periods:
            work_time += work_period.get_time_spent()
        return work_time