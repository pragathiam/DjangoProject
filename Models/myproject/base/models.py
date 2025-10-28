from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)

class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField(default=0)
    course=models.CharField(max_length=100)

    