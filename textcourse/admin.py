from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import MPTTArticle, Course
# Register your models here.
from .forms import ArticleForm
 
class MPTTArticleInline(admin.TabularInline):

    model = MPTTArticle
    extra = 1
    max_num = 50

class MPTTArticleAdmin(MPTTModelAdmin):
    list_display = [
        'index',        
        'title',
        'order',
        'course',
    ]

    list_filter = [
        'course'
    ]

    # list_editable = ["order",]

    form = ArticleForm


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        # MPTTArticleInline,
    ]

admin.site.register(MPTTArticle, MPTTArticleAdmin)
admin.site.register(Course, CourseAdmin)