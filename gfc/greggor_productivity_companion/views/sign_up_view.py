from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from greggor_productivity_companion.forms import UserSignUpForm
from ..models import User
from django.contrib import messages
from ..helpers import offline_required

@offline_required
def sign_up_view(request: HttpRequest) -> HttpResponse:
    """View for the user to create an account"""
    if request.method == 'POST':
        form: UserSignUpForm = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user: User = form.save()
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "You have successfully created an account")
            return redirect('dashboard')
    else:
        form: UserSignUpForm = UserSignUpForm()
    return render(request, "pages/sign_up.html", {'form': form})