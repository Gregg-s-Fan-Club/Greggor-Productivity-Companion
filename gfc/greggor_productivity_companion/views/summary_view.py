from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from greggor_productivity_companion.models import Task, User
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models import QuerySet


@login_required
def summary_view(request: HttpRequest) -> HttpResponse:
    """View to see summary"""
    user: User = request.user
    user_tasks = Task.objects.filter(user=user.id)
    recent_tasks = user_tasks[0:3]

    context: dict[str, Any] = {
        'tasks': recent_tasks
    }


    return render(request, "pages/summary.html", context)
