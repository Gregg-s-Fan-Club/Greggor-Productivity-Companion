from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import User
from django.contrib import messages
from ..helpers import level_icons


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    """View to display user profile"""
    icons = request.user.unlocked_icons()
    return render(request, 'pages/profile.html',
                  {'profile_icons': icons})

@login_required
def profile_change_icon(request: HttpRequest, icon_name) -> HttpResponse:
    """View to display user profile"""
    user = request.user
    icons = user.unlocked_icons()

    if icon_name in icons:
        user.profile_icon = icon_name
        user.save()

    return redirect('profile')



@login_required
def delete_profile_view(request: HttpRequest) -> HttpResponse:
    """View to delete user"""
    user: User = request.user
    user.delete()
    messages.add_message(
        request,
        messages.WARNING,
        "Your profile has been deleted")
    return redirect('log_in')
