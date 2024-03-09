from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..models import Task, User
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from greggor_productivity_companion.helpers import paginate
from django.core.paginator import Page


@login_required
def display_tasks_view(request: HttpRequest) -> HttpResponse:
    """View to display the users transactions"""
    user: User = request.user

    list_of_tasks = user.get_user_tasks()

    # task: list[Task] = sorted(
    #     list(
    #         dict.fromkeys(
    #             user.get_user_transactions(filter_type))),
    #     key=lambda x: x.time_of_transaction,
    #     reverse=True)

    list_of_tasks: Page = paginate(
        request.GET.get('page', 1), list_of_tasks)

    return render(request, "pages/display_tasks.html",
                  {'tasks': list_of_tasks})
