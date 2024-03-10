from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Category, WorkPeriod, Task


@admin.register(User)
class User(admin.ModelAdmin):
    """Configuration of the admin interface for user."""

    list_display = [
        'id', 'username', 'email', 'profile_icon']

@admin.register(Category)
class Category(admin.ModelAdmin):
    """Configuration of the admin interface for user."""

    list_display = [
        'id', 'name', 'max_points_per_cycle']

@admin.register(Task)
class Task(admin.ModelAdmin):
    """Configuration of the admin interface for task."""

    list_display = [
        'id', 'user', 'name', 'description', 'expected_work_time','category','completed', 'bonus_points']

@admin.register(WorkPeriod)
class WorkPeriod(admin.ModelAdmin):
    """Configuration of the admin interface for WorkPeriod."""

    list_display = [
        'id', 'date', 'start_time', 'end_time','task', 'points']