from django.contrib import admin

# Register your models here.
from .models import Activity, Task

admin.site.register(Activity)
admin.site.register(Task)
