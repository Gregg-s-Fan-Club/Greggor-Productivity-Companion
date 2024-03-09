from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..models import WorkPeriod, Task
from ..forms import WorkPeriodForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from greggor_productivity_companion.helpers import paginate
from django.core.paginator import Page
from django.contrib import messages
from itertools import chain

@login_required
def display_work_period_view(request: HttpRequest, task_type="ALL") -> HttpRequest:
    if task_type != "ALL":
        tasks = Task.objects.filter(user = request.user, name=task_type)
    else:
        tasks = Task.objects.filter(user = request.user)

    work_periods = WorkPeriod.objects.filter(task = tasks[0])
    for task in tasks:
       work_periods = WorkPeriod.objects.filter(task = task) | work_periods
    work_periods = paginate(request.GET.get('page', 1), work_periods)
    return render(request, "pages/display_work_periods.html", {'work_periods': work_periods, 'tasks': tasks})

@login_required
def filter_task_type_request(request) -> HttpResponse:
    """Filters transactions and sets redirect to input page with filter"""
    return redirect("display_work_period_view", request.POST['task'])

def create_work_period(request: HttpRequest) -> HttpResponse:

    user = request.user
    if request.method == 'POST':
        form = WorkPeriodForm(user,request.POST)
        if form.is_valid():
            form.save(user)
            messages.add_message(
                request, messages.SUCCESS, "Your work period has been added successfully")
            return redirect('dashboard',)
    else:
        form = WorkPeriodForm(user)
    return render(request, "pages/add_work_period.html", {'form': form, 'edit': False})

def edit_work_periods(request: HttpRequest, pk):

    try:
        work_period = WorkPeriod.objects.get(id=pk)
        user = request.user
        if(work_period.task.user != user):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This work period cannot be edited")
        return redirect('dashboard')
    
    if request.method =='POST':
        form = WorkPeriodForm(
            user, request.POST, instance = work_period)
        if form.is_valid():
            form.save(instance = work_period)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your work period has been successfully updated")
            return redirect('dashboard',)
    else:
        form = WorkPeriodForm(user,instance=work_period)
    return render(request, "pages/add_work_period.html",
                  {'form': form, 'edit': True,'pk': pk})

def delete_work_period(request: HttpRequest, pk) -> HttpResponse:
    """View to delete a task"""
    try:
        work_period = WorkPeriod.objects.get(id=pk)
        task: Task = request.task
        if (work_period.task != task):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This task cannot be deleted.")
        return redirect('dashboard')
    else:
        work_period.delete()
        messages.add_message(
            request,
            messages.WARNING,
            "The transaction has been deleted")
        return redirect('dashboard')