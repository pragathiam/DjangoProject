from django.db import models

# Create your models here.
class flightbookingdetails(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

class flightbookingconfirmation(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)    