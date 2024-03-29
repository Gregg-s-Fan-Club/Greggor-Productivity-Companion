from django import forms
from ..models.user_model import User
from typing import Any


class EditUserDetailsForm(forms.ModelForm):
    "Form to edit a user's details"
    class Meta:
        model: User = User
        fields: list[str] = [
            'username',
            'email'
            ]
        
