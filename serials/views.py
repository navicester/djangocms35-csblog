from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
class SerialListView(ListView):
    queryset = Serial.objects.filter(active=True)
    template_name = "serials_list.html"

class SerialDetailView(DetailView):
    queryset = Serial.objects.all()
    template_name = "serials_detail.html"   

    def get_context_data(self, *args, **kwargs):
        context = super(SerialDetailView, self).get_context_data(*args, **kwargs) 
        context["object_list"] = Entry.objects.filter(serial__pk=self.get_object().pk, active=True)

        return context