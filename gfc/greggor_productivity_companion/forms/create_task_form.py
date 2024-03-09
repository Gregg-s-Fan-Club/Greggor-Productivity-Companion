from django import forms
from greggor_productivity_companion.models import Task, Category
from typing import Any


class TaskForm(forms.ModelForm):
    """Form to add a new task"""

    class Meta:
        model = Task
        fields = ['name', 'description', 'expected_work_time','actual_work_time','completed']
        widgets = {'description': forms.Textarea()}
        
        category: forms.ChoiceField = forms.ChoiceField(choices=Category.objects.all(), label="Category"
    )

    def save(self, current_user, category, instance = None) :
        """Create a new task."""
        super().save(commit=False)
        if instance is None:
            task = Task.objects.create(
                user=current_user,
                name=self.cleaned_data.get('name'),
                description=self.cleaned_data.get('description'),
                category = self.cleaned_data.get('Category'),
                expected_work_time =  self.cleaned_data.get('expected_work_time'),
                actual_work_time =  self.cleaned_data.get('actual_work_time'),
                completed =  self.cleaned_data.get('completed')
            )
        else:
            task = instance
            task.name = self.cleaned_data.get('name')
            task.description = self.cleaned_data.get('description')
            task.category = self.cleaned_data.get('Category')
            task.expected_work_time = self.cleaned_data.get('expected_work_time')
            task.actual_work_time =  self.cleaned_data.get('actual_work_time')
            task.completed =  self.cleaned_data.get('completed')

            task.save()

        return task