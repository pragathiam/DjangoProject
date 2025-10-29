from django.db import models

# Create your models here.

class StudentsModel(models.Model):
    s_name=models.CharField(max_length=100)
    s_rollno=models.IntegerField(default=0)
    s_course=models.CharField(max_length=200)