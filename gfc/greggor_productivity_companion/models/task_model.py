from django.db import models
from greggor_productivity_companion.models import User, Category
from greggor_productivity_companion import models as gfc


class Task(models.Model):
    """Task model used for different productivity tasks"""
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    name: models.CharField = models.CharField(max_length=520, blank=False)
    description: models.CharField = models.CharField(max_length=520)
    expected_work_time: models.DurationField = models.DurationField(blank=False)
    actual_work_time: models.DurationField = models.DurationField(blank=False)
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)
    completed: models.BooleanField = models.BooleanField(default=False)
    bonus_points = models.IntegerField(blank=False, default=0)
    
    def get_user_tasks_for_category(self) -> list:
            """Return list of the users transactions"""
            tasks: list[fcmodels.Tasks] = fcmodels.Task.objects.filter(
                user=self, category=filter_type)

            return tasks

    class Meta:
        unique_together = ['user', 'name', 'category']


    def get_task_points(self):
        work_periods = gfc.WorkPeriod.objects.filter(user = self)
        points = 0
        for period in work_periods:
            points += period.points
        return points


