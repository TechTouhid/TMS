from django.contrib import admin

# Register your models here.
from .models import Activity, Assignment
from .forms import Task

admin.site.register(Activity)
admin.site.register(Task)
admin.site.register(Assignment)
