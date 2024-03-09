from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
import greggor_productivity_companion.models as fcmodels

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
    points = models.IntegerField(blank=False, default = 0)

    def get_user_tasks(self, filter_type: str = "all") -> list:
            """Return list of the users transactions"""
            tasks: list[fcmodels.Tasks] = fcmodels.Task.objects.filter(
                user=self)

            return tasks
