from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

class HistoryModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)