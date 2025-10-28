from django.db import models

# Create your models here.
class Booking(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()


class cancelling(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()