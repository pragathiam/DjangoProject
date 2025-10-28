from django.contrib import admin

# Register your models here.

from base.models import StudentModel,ArticleModel

class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
    list_display_links=['title']


admin.site.register(ArticleModel,ArticleAdmin)

admin.site.register(StudentModel)