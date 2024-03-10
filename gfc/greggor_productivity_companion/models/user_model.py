from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
import greggor_productivity_companion.models as gpcmodels
from ..helpers import GreggorTypes, level_icons

class User(AbstractUser):
    """User model used for authentication"""

    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{1,}$',
            message='Username must consist of @ followed by at least one letter or number'
        )]
    )
    email = models.EmailField(unique=True, blank=False)
    profile_icon = models.CharField(max_length=30, default=GreggorTypes.NORMAL)

    def get_user_points(self, category_type = "ALL"):
        tasks = self.get_user_tasks(category_type)
        points = 0
        for task in tasks:
            points += task.get_task_points()
        return points
            
    def get_user_tasks(self, category_type = "ALL"):
        if category_type == "ALL":
            return gpcmodels.Task.objects.filter(user = self)
        else:
            return gpcmodels.Task.objects.filter(user = self, category = category_type)

    def get_level(self):
        return min(6, round(self.get_user_points()/100))
    
    def unlocked_icons(self):
        level = self.get_level()
        if level in level_icons.keys():
            return level_icons[level]
        

        return level_icons[0]