from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from greggor_productivity_companion.models import User, Category, Task
from django.contrib.auth.decorators import login_required


def dashboard_view(request):
    
    context = {}

    return render(request, "pages/dashboard.html", context)