from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import MPTTArticle, Course
# Register your models here.
 
admin.site.register(MPTTArticle, MPTTModelAdmin)
admin.site.register(Course)