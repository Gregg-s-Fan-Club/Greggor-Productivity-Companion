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
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, date

@login_required
def display_work_period_view(request: HttpRequest, task_type="ALL", start_date = "2016-01-01", end_date="2140-07-22") -> HttpRequest:
    if task_type != "ALL":
        tasks = Task.objects.filter(user = request.user, name=task_type)
    else:
        tasks = Task.objects.filter(user = request.user)
    allTasks  = Task.objects.filter(user = request.user)
    startObj = datetime.strptime(start_date, "%Y-%m-%d")
    endObj = datetime.strptime(end_date, "%Y-%m-%d")
    work_periods = WorkPeriod.objects.filter(task = tasks[0], date__range=(startObj.date(), endObj.date()))
    for task in tasks:
       work_periods = WorkPeriod.objects.filter(task = task, date__range=(startObj.date(), endObj.date())) | work_periods
    work_periods = paginate(request.GET.get('page', 1), work_periods)
    return render(request, "pages/display_work_periods.html", {'work_periods': work_periods, 'tasks': allTasks})

@login_required
def filter_task_type_request(request) -> HttpResponse:
    """Filters transactions and sets redirect to input page with filter"""
    return redirect("display_work_period_view", request.POST['task'], request.POST['start_date'], request.POST['end_date'])

def create_work_period(request: HttpRequest) -> HttpResponse:

    user = request.user
    if request.method == 'POST':
        form = WorkPeriodForm(user, request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your work period has been added successfully")
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
            user, request.POST, instance=work_period)
        if form.is_valid():
            form.save(instance=work_period)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your work period has been successfully updated")
            return redirect('view_individual_work_period',pk)
    else:
        form = WorkPeriodForm(user,instance=work_period)
    return render(request, "pages/add_work_period.html",
                  {'form': form, 'edit': True,'pk': pk})

def delete_work_period(request: HttpRequest, pk) -> HttpResponse:
    """View to delete a task"""
    try:
        work_period = WorkPeriod.objects.get(id=pk)
        user = request.user
        if (work_period.task.user != user):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This work period cannot be deleted.")
        return redirect('dashboard')
    else:
        work_period.delete()
        messages.add_message(
            request,
            messages.WARNING,
            "The work period has been deleted")
        return redirect('dashboard')

def view_individual_work_period(request: HttpRequest, pk) -> HttpResponse:
    """View to view a work period"""
    try:
        work_period = WorkPeriod.objects.get(id=pk)
        user: User = request.user
        if (work_period.task.user != user):
            return redirect('dashboard')
    except ObjectDoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "This work period cannot be accessed.")
        return redirect('dashboard')
    else:
        
        return render(request, "partials/view_individual_work_period.html",
                  {'work_period': work_period})
