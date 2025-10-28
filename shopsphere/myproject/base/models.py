from django.db import models

# Create your models here.
class Products(models.Model):
    p_category=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_desc=models.CharField(max_length=100)
    p_price=models.CharField(max_length=100)
    p_image=models.ImageField(default='default.webp',upload_to='uploads')


class cartModel(models.Model):
    p_category=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_desc=models.CharField(max_length=100)
    p_price=models.CharField(max_length=100)
    

