from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Activity(models.Model):
    activity_id = models.AutoField(User, primary_key=True)
    title = models.CharField(max_length=120, verbose_name='Title')
    description = models.TextField(null=False, verbose_name='Description')

    def __str__(self):
        return self.title


class Task(models.Model):
    activity_task_id = models.ForeignKey(Activity, default=0)
    task_name = models.CharField(max_length=120, verbose_name='Task name')
    start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Start date')
    end_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='End date')
    start_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Start Time')
    end_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='End Time')

    def __str__(self):
        return self.task_name


class Assignment(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True)
    supervisor = models.ForeignKey(User, null=True, blank=True, related_name='Supervisor')
    assigned_employee = models.ForeignKey(User, null=True, blank=True, related_name='Assigned_Employee')
    duration = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Duration')
    note = models.TextField(null=True, blank=True, verbose_name='Note')
    cost = models.IntegerField(null=True, blank=True, verbose_name='Cost')

