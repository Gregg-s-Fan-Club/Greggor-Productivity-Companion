from django import forms
from greggor_productivity_companion.models import WorkPeriod, Task
from typing import Any
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime, date




class WorkPeriodForm(forms.ModelForm):
    """form to add a new work period"""

    def __init__(self, user, *args, **kwargs):
        super(WorkPeriodForm,self).__init__(*args, **kwargs)

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
        print(cleaned_data)
        if 'date' in self.cleaned_data.keys():
            date = self.cleaned_data['date']

            if date > date.today():
                self.add_error('date', 'Date is in future')
            end_time = self.cleaned_data['end_time']
            start_time = self.cleaned_data['start_time']
            if end_time < start_time:
                self.add_error('end_time', 'End time is before start time')
            
            # super().clean()
            print(cleaned_data)
            # cleaned_data = self.cleaned_data
            if WorkPeriod.objects.filter(date=date,         
                                    task=cleaned_data['task'],
                                    start_time=start_time, end_time=end_time).exists():
                self.add_error('date', 'workPeriod with this date, task, start time and end time exists')


    def calculatePoints(self):
        end_time = self.cleaned_data['end_time']
        start_time = self.cleaned_data['start_time']
        difference = datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time)
        minutes = int(difference.total_seconds() / 60)

        task = self.cleaned_data['task']
        self.get_total_points_for_current_cycle()
        return min(task.category.max_points_per_cycle, 0.5 * minutes)
    
    def get_total_points_for_current_cycle(self):
        print(date.today().weekday())

    def save(self, current_user, instance = None):
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
            workPeriod.task = self.cleaned_data.get('Task')

            workPeriod.save()
        
        return workPeriod