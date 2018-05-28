from django.db import models


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, verbose_name='Title')
    description = models.TextField(null=False, verbose_name='Description')


class Task(Activity, models.Model):
    task_name = models.CharField(max_length=120, verbose_name='Task name')
    start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Start date')
    end_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='End date')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Start Time')
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Start Time')


class Assignment(models.Model):
    duration = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Duration')
    note = models.TextField(null=True, blank=True, verbose_name='Note')
    cost = models.IntegerField(null=True, blank=True, verbose_name='Cost')
