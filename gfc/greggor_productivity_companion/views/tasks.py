from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..models import Task, User, Category
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from greggor_productivity_companion.helpers import paginate
from django.core.paginator import Page

@login_required
def display_tasks_view(request: HttpRequest, filter_type: "ALL") -> HttpResponse:
    """View to display the users transactions"""
    user: User = request.user
    categories = Category.objects.all()
    if filter_type != "ALL":
        list_of_tasks = Task.objects.filter(user=user, category = Category.objects.filter(name=filter_type)[0])
    else:
        list_of_tasks = Task.objects.filter(user=user)
    # task: list[Task] = sorted(
    #     list(
    #         dict.fromkeys(
    #             user.get_user_transactions(filter_type))),
    #     key=lambda x: x.time_of_transaction,
    #     reverse=True)

    list_of_tasks: Page = paginate(
        request.GET.get('page', 1), list_of_tasks)

    return render(request, "pages/display_tasks.html",
                  {'tasks': list_of_tasks, 'categories': categories})

@login_required
def filter_task_request(request) -> HttpResponse:
    """Filters transactions and sets redirect to input page with filter"""
    return redirect("display_tasks", request.POST['category'])
    

