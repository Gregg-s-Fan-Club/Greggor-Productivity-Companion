from django import forms
from greggor_productivity_companion.models import WorkPeriod, Task
from typing import Any


class WorkPeriodForm(forms.ModelForm):
    """form to add a new work period"""

    def __init__(self, *args, **kwargs):
        super(WorkPeriodForm,self).__init__(*args, **kwargs)

        self.fields['task'].queryset = Task.objects.all()
        self.fields['task'].label_from_instance: str = self.label_from_instance

    def label_from_instance(self, obj) -> str:
        """Return objects name"""
        return obj.name

    class Meta:
        model = WorkPeriod
        fields = ['date', 'start_time', 'end_time', 'task']
        widgets = {'date': forms.DateField(), 'start_time': forms.TimeField(), 'end_time': forms.TimeField()}

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