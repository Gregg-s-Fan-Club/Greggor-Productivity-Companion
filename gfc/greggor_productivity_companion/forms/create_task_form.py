from django import forms
from greggor_productivity_companion.models import Task, Category
from typing import Any


class TaskForm(forms.ModelForm):
    """Form to add a new task"""

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.user = user
        # self.instance = kwargs.get("instance")
        
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].label_from_instance: str = self.label_from_instance
    
    def label_from_instance(self, obj) -> str:
        """Return objects name"""
        return obj.name

    class Meta:
        model = Task
        fields = ['name', 'description', 'expected_work_time','completed', 'category']
        widgets = {'description': forms.Textarea(),'expected_work_time': forms.TextInput(attrs={'placeholder': 'hh:mm:ss', 'class': 'form-control'})}
        


    def clean(self):
        super().clean()
        check_unique_together: models.QuerySet[AbstractTarget] = Task.objects.filter(
            user=self.user,name= self.cleaned_data.get('name'),         
                                    category= self.cleaned_data.get('category'))

        if self.instance is None:
            if len(check_unique_together) > 0:
                self.add_error('name', 'Task with this name and category exists')
                self.add_error('category', 'Task with this name and category exists')
        else:
            if any(check_unique_target_object !=
                   self.instance for check_unique_target_object in check_unique_together):
                self.add_error('name', 'Task with this name and category exists')
                self.add_error('category', 'Task with this name and category exists')



        

    def save(self, instance = None) :
        """Create a new task."""
        super().save(commit=False)
       
        if instance is None:
            task = Task.objects.create(
                user=self.user,
                name=self.cleaned_data.get('name'),
                description=self.cleaned_data.get('description'),
                category = self.cleaned_data.get('category'),
                expected_work_time =  self.cleaned_data.get('expected_work_time'),
                completed =  self.cleaned_data.get('completed')
            )
        else:
            task = instance
            databaseTask = Task.objects.filter(id = task.id)[0]

            if databaseTask.completed == False and self.cleaned_data.get('completed') == True:
                actual_work_time = task.get_actual_work_time()
                latest_workflow = task.get_latest_task_workflow()
                bonus_points = round(100 - abs(((task.expected_work_time - actual_work_time) / actual_work_time) * 100))
                print(latest_workflow.get_remaining_points_for_current_cycle(), bonus_points)
                latest_workflow.points += min(latest_workflow.get_remaining_points_for_current_cycle(), bonus_points)
                latest_workflow.save()
                task.bonus_points = bonus_points
            elif databaseTask.completed == True and self.cleaned_data.get('completed') == False:
                latest_workflow = task.get_latest_task_workflow()
                latest_workflow.points -= task.bonus_points
                latest_workflow.save()
                task.bonus_points = 0

            task.name = self.cleaned_data.get('name')
            task.description = self.cleaned_data.get('description')
            task.category = self.cleaned_data.get('category')
            task.expected_work_time = self.cleaned_data.get('expected_work_time')
            task.completed =  self.cleaned_data.get('completed')
                
            task.save()

        return task