from django.db import models

# Create your models here.
class BookingDetails(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()


class BookingConfirmation(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()