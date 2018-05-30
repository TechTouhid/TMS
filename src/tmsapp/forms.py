from django import forms
from .models import Activity, Assignment, Task


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ['activity_task_id', 'task_name', 'start_date', 'end_date', 'start_time', 'end_time']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['task', 'supervisor', 'assigned_employee', 'duration', 'note', 'cost']
