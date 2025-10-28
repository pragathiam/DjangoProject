from django.contrib import admin
from base.models import TaskModel

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=['title','desc']

admin.site.register(TaskModel,TaskAdmin)