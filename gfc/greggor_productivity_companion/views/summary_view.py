from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from greggor_productivity_companion.models import Task, User, WorkPeriod
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models import QuerySet
from datetime import datetime, timedelta

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

    

    


    context: dict[str, Any] = {
        'tasks': recent_tasks, 
        'hours_spent_month': total_hours_month,
        'hours_spent_week': total_hours_week,
        'hours_spent_day' : total_hours_day
    }


    return render(request, "pages/summary.html", context)

