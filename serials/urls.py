from django.conf import settings
from django.conf.urls import include, url

from .views import (
    SerialListView, 
    SerialDetailView,
)

urlpatterns = [
    url(r'^$', SerialListView.as_view(), name='serial_list'), 
    url(r'^(?P<pk>\d+)', SerialDetailView.as_view(), name='serial_detail'), 
]