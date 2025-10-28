from django.contrib import admin

# Register your models here.
from base.models import Products
class ProductAdminModel(admin.ModelAdmin):
    list_display=['p_category','p_name','p_desc','p_price']

admin.site.register(Products,ProductAdminModel)