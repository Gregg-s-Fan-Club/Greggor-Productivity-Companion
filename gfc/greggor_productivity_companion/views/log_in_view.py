from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from greggor_productivity_companion.forms import UserLogInForm
from django.contrib.auth.decorators import login_required
from ..models import User
from ..helpers import offline_required

@offline_required
def log_in_view(request: HttpRequest) -> HttpResponse:
    """View for users to log in"""
    if request.method == 'POST':
        form: UserLogInForm = UserLogInForm(request.POST)
        if form.is_valid():
            username: str = form.cleaned_data.get('username')
            password: str = form.cleaned_data.get('password')
            user: User = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url: str = request.POST.get('next') or 'dashboard'
                return redirect(redirect_url)
        messages.add_message(
            request,
            messages.ERROR,
            "The credentials provided are invalid!")
    form: UserLogInForm = UserLogInForm()
    next_page: str = request.GET.get('next') or ''
    return render(request, 'pages/log_in.html',
                  {'form': form, 'next': next_page})


@login_required
def log_out_view(request) -> HttpResponse:
    """View for users to logout"""
    logout(request)
    messages.add_message(
        request,
        messages.SUCCESS,
        "You've logged out successfully")
    return redirect('log_in')