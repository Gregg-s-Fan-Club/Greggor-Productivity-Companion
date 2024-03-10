from django import forms
from greggor_productivity_companion.models import WorkPeriod, Task
from typing import Any
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime, date, timedelta

class WorkPeriodForm(forms.ModelForm):
    """form to add a new work period"""

    def __init__(self, user, *args, **kwargs):
        super(WorkPeriodForm,self).__init__(*args, **kwargs)
        self.user = user
        # self.instance = kwargs.get("instance")

        self.fields['task'].queryset = Task.objects.filter(user = user)
        self.fields['task'].label_from_instance: str = self.label_from_instance

    def label_from_instance(self, obj) -> str:
        """Return objects name"""
        return obj.name

    class Meta:
        model = WorkPeriod
        fields = ['date', 'start_time', 'end_time', 'task']
        widgets = {'date': forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            ), 'start_time' : forms.TimeInput(attrs={'type': 'time'}), 'end_time' :  forms.TimeInput(attrs={'type': 'time'})}

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        date = self.cleaned_data['date']
        end_time = self.cleaned_data['end_time']
        start_time = self.cleaned_data['start_time']
        check_unique_together = WorkPeriod.objects.filter(date=date,         
                                    task=cleaned_data['task'],
                                    start_time=start_time, end_time=end_time)

        if date > date.today():
            self.add_error('date', 'Date is in future')
        
        if end_time < start_time:
            self.add_error('end_time', 'End time is before start time')
        
        if self.instance is None:
            if len(check_unique_together) > 0:
                self.add_error('end_time', 'Task with this date, start time and end time exists')
                self.add_error('start_time', 'Task with this date, start time and end time exists')
                self.add_error('date', 'Task with this date, start time and end time exists')
        else:
            if any(check_unique_target_object !=
                    self.instance for check_unique_target_object in check_unique_together):
                self.add_error('end_time', 'Task with this date, start time and end time exists')
                self.add_error('start_time', 'Task with this date, start time and end time exists')
                self.add_error('date', 'Task with this date, start time and end time exists')

    def calculatePoints(self, start_time, end_time, work_period):
        difference = datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time)
        minutes = int(difference.total_seconds() / 60)

        return min(work_period.get_remaining_points_for_current_cycle(), 0.5 * minutes)
        


    def save(self, instance=None):
        super().save(commit=False)

        date=self.cleaned_data.get('date')
        start_time=self.cleaned_data.get('start_time')
        end_time=self.cleaned_data.get('end_time')
        task = self.cleaned_data.get('task')

        if instance is None:
            print(1353443564)
            work_period = WorkPeriod.objects.create(
                date = date,
                start_time = start_time,
                end_time = end_time,
                points = 0,
                task = task,
            )

            # work_period.points = self.calculatePoints(start_time[0], end_time[0], work_period)
            # work_period.save()
        else:
            work_period = instance
            work_period.date = self.cleaned_data.get('date')
            work_period.start_time = self.cleaned_data.get('start_time')
            work_period.end_time = self.cleaned_data.get('end_time')
            work_period.points = self.calculatePoints(start_time, end_time, work_period)
            work_period.task = self.cleaned_data.get('task')

            work_period.save()
        
        return work_period