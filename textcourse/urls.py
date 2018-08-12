from django.conf import settings
from django.conf.urls import include, url

from .views import (
    course_list, 
    course_detail,
    article_list, 
    article_detail,
)

urlpatterns = [
    url(r'^$', course_list, name='course_list'), 
    url(r'^(?P<pk>\d+)/$', course_detail, name='course_detail'), 
    url(r'^articles$', article_list, name='article_list'), 
    url(r'^article/(?P<pk>\d+)$', article_detail, name='article_detail'), 
]