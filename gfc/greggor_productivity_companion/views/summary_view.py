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

    last_month = datetime.today() - timedelta(days=30)

    total_hours = 0
    for task in user_tasks: 
        task_workflows = WorkPeriod.objects.filter(date__gte=last_month, task=task)
        for flow in task_workflows:
            total_hours += flow.get_hours_spent()





    context: dict[str, Any] = {
        'tasks': recent_tasks, 
        'hours_spent': total_hours
    }


    return render(request, "pages/summary.html", context)
