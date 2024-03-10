from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from greggor_productivity_companion.models import Task, User, WorkPeriod
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models import QuerySet
from datetime import datetime, timedelta
from ..helpers import category_bar_chart_data

@login_required
def summary_view(request: HttpRequest) -> HttpResponse:
    """View to see summary"""
    user: User = request.user
    user_tasks = Task.objects.filter(user=user.id)
    recent_tasks = user_tasks[0:3]

    # def period_hours(tasks, amount):
    #     last_month = datetime.today() - timedelta(days=amount)
    #     total_hours = 0
    #     for task in tasks: 
    #         task_workflows = WorkPeriod.objects.filter(date__gte=last_month, task=task)
    #         print(type(task_workflows))
    #         for flow in task_workflows:
    #             total_hours += flow.get_hours_spent()
    #     return total_hours
    
    def combined_workflows(tasks, period):
        combined = []
        for task in tasks:
            combined = combined + list(task.get_task_workflows_over_period(period))
        return combined
    
    def total_hours(workflows):
        hours = 0
        for flow in workflows:
            hours += flow.get_hours_spent()
        return hours


    workflows_month = combined_workflows(user_tasks, 30)
    workflows_week = combined_workflows(user_tasks, 7)
    workflows_day = combined_workflows(user_tasks, 1)

    total_hours_month = total_hours(workflows_month)
    total_hours_week = total_hours(workflows_week)
    total_hours_day = total_hours(workflows_day)

    day_dict_hours = {}
    for flow in workflows_month:
        date = flow.date
        if date not in day_dict_hours:
            day_dict_hours[date] = flow.get_hours_spent() 
        else:
            day_dict_hours[date] += flow.get_hours_spent() 
    day_values_hours = list(day_dict_hours.values())
    day_keys_hours = list(day_dict_hours.keys())

    if len(day_values_hours) != 0:
        highest_day_hours = day_keys_hours[day_values_hours.index(max(day_values_hours))]
        lowest_day_hours = day_keys_hours[day_values_hours.index(min(day_values_hours))]
    else:
        highest_day_hours = "N/A"
        lowest_day_hours = "N/A"
    

    day_dict_points = {}
    for flow in workflows_month:
        date = flow.date
        if date not in day_dict_points:
            day_dict_points[date] = flow.points
        else:
            day_dict_points[date] += flow.points
    day_values_points = list(day_dict_points.values())
    day_keys_points = list(day_dict_points.keys())

    if len(day_values_points) != 0:
        highest_day_points = day_keys_points[day_values_points.index(max(day_values_points))]
        lowest_day_points = day_keys_points[day_values_points.index(min(day_values_points))]
    else:
        highest_day_points = "N/A"
        lowest_day_points = "N/A"





    context: dict[str, Any] = {
        'tasks': recent_tasks, 
        'hours_spent_month': round(total_hours_month,2),
        'hours_spent_week': round(total_hours_week,2),
        'hours_spent_day' : total_hours_day,
        'highest_day_hours': highest_day_hours,
        'lowest_day_hours': lowest_day_hours,
        'highest_day_points': highest_day_points,
        'lowest_day_points': lowest_day_points,
        'user_workflow_data': category_bar_chart_data(request.user)
    }


    return render(request, "pages/summary.html", context)

