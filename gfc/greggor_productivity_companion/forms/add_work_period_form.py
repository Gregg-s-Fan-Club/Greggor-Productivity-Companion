from django import forms
from greggor_productivity_companion.models import WorkPeriod, Task
from typing import Any


class WorkPeriodForm(forms.ModelForm):
    """form to add a new work period"""

    class Meta:
        model = WorkPeriod
        date = forms.DateInput()
        start_time = forms.TimeField()
        end_time = forms.TimeField()
        fields = ['Date', 'start_time', 'end_time']

        task = forms.ChoiceField(choices=Task.objects.all(), label="Task")

    def save(self, current_user, task, instance = None):

        super().save(commit=False)
        if instance is None:
            workPeriod = WorkPeriod.objects.create(
                date=self.cleaned_data.get('date'),
                start_time=self.cleaned_data.get('start_time'),
                end_time=self.cleaned_data.get('end_time'),
                points=1,
                task = self.cleaned_data.get('Task')
            )
        else:
            workPeriod = instance
            workPeriod.date = self.cleaned_data.get('date'),
            workPeriod.start_time = self.cleaned_data.get('start_time'),
            workPeriod.end_time = self.cleaned_data.get('end_time'),
            workPeriod.points = 1,
            workPeriod.task = self.cleaned_data.get('Task')

            task.save()
        
        return workPeriod