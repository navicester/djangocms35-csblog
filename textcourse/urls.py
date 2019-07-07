from django.conf import settings
from django.conf.urls import include, url

from .views import (
    course_list, 
    course_detail,
    article_list, 
    article_detail,
    article_search_list,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    url(r'^$', course_list, name='course_list'), 
    url(r'^(?P<pk>\d+)/$', course_detail, name='course_detail'), 
    url(r'^(?P<pk>\d+)/create$', ArticleCreateView.as_view(), name='article_create'), 
    url(r'^articles$', article_list, name='article_list'), 
    url(r'^articles/search$', article_search_list, name='article_search'), 
    url(r'^(?P<pk1>\d+)/article/(?P<pk>\d+)$', article_detail, name='article_detail'), 
    url(r'^(?P<pk1>\d+)/article/(?P<pk>\d+)/update/$', ArticleUpdateView.as_view(), name='article_update'),    
    url(r'^(?P<pk1>\d+)/article/(?P<pk>\d+)/delete/$', ArticleDeleteView.as_view(), name='article_delete'),   
]