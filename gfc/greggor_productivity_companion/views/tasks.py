from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..models import Task, User, Category
from ..forms import TaskForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from greggor_productivity_companion.helpers import paginate
from django.core.paginator import Page
from django.contrib import messages


@login_required
def display_tasks_view(request: HttpRequest, filter_type = "ALL") -> HttpResponse:
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
    

def create_tasks(request: HttpRequest) -> HttpResponse:
    """View to create a task"""

    user: User = request.user
    if request.method == 'POST':
        form = TaskForm(
            user, request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your task has been successfully added")
            return redirect('dashboard',)
    else:
        form = TaskForm(user)
    return render(request, "pages/add_task.html",
                  {'form': form, 'edit': False})

def edit_tasks(request: HttpRequest, pk) -> HttpResponse:
    """View to edit a task"""

    try:
        task = Task.objects.get(id=pk)
        user: User = request.user
        if (task.user != user):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This task cannot be edited.")
        return redirect('dashboard')


    if request.method == 'POST':
        form = TaskForm(
            user, request.POST, instance = task)
        if form.is_valid():
            form.save(instance = task)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your task has been successfully updated")
            return redirect('dashboard',)
    else:
        form = TaskForm(user, instance=task)
    return render(request, "pages/add_task.html",
                  {'form': form, 'edit': True,'pk': pk})

def delete_tasks(request: HttpRequest, pk) -> HttpResponse:
    """View to delete a task"""
    try:
        task = Task.objects.get(id=pk)
        user: User = request.user
        if (task.user != user):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This task cannot be deleted.")
        return redirect('dashboard')
    else:
        task.delete()
        messages.add_message(
            request,
            messages.WARNING,
            "The transaction has been deleted")
        return redirect('dashboard')

def view_individual_task(request: HttpRequest, pk) -> HttpResponse:
    """View to view a task"""
    try:
        task = Task.objects.get(id=pk)
        user: User = request.user
        if (task.user != user):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This task cannot be deleted.")
        return redirect('dashboard')
    else:
        
        return render(request, "partials/view_individual_task.html",
                  {'task': task})