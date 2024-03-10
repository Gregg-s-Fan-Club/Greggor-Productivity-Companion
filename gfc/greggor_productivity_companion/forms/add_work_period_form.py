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


    def calculatePoints(self):
        end_time = self.cleaned_data['end_time']
        start_time = self.cleaned_data['start_time']
        difference = datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time)
        minutes = int(difference.total_seconds() / 60)

        task = self.cleaned_data['task']
        print(self.get_total_points_for_current_cycle())
        return min(self.get_total_points_for_current_cycle(), 0.5 * minutes)
    
    def get_total_points_for_current_cycle(self):
        date = self.cleaned_data['date']
        start_date = date - timedelta(days=date.today().weekday())
        end_date = start_date +  timedelta(days=7)
        points = 0
        task = self.cleaned_data['task']
        workperiods = WorkPeriod.objects.filter(task=task)
        for workperiod in workperiods:
            if workperiod.date >= start_date and workperiod.date <= end_date:
                points = points + workperiod.points
        
        max_points = task.category.max_points_per_cycle

        if points > max_points:
            return 0
        else:
            return max_points - points
        


    def save(self, instance=None):
        super().save(commit=False)
        self.calculatePoints()
        if instance is None:
            workPeriod = WorkPeriod.objects.create(
                date=self.cleaned_data.get('date'),
                start_time=self.cleaned_data.get('start_time'),
                end_time=self.cleaned_data.get('end_time'),
                points=self.calculatePoints(),
                task = self.cleaned_data.get('task')
            )
        else:
            workPeriod = instance
            workPeriod.date = self.cleaned_data.get('date')
            workPeriod.start_time = self.cleaned_data.get('start_time')
            workPeriod.end_time = self.cleaned_data.get('end_time')
            workPeriod.points = self.calculatePoints()
            workPeriod.task = self.cleaned_data.get('task')

            workPeriod.save()
        
        return workPeriod