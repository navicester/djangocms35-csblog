from django.shortcuts import render, render_to_response

# Create your views here.
from .models import MPTTArticle, Course

def course_list(request):
    object_list= Course.objects.all()
     
    return render(request, 'course_list.html', {'object_list': object_list})

def course_detail(request, pk):
    node= Course.objects.get(pk=pk)
     
    return render(request, 'course_detail.html', {
            'object': node,
    })    

def article_list(request):
    # nodes= MPTTArticle.objects.root_nodes()
    nodes= MPTTArticle.objects.filter(parent=None)
     
    return render(request, 'article_list.html', {'nodes': nodes})


def article_detail(request, pk1, pk):
    articles = MPTTArticle.objects.filter(course__id=pk1)
    node= articles.get(pk=pk)
    nodes= articles
     
    return render(request, 'article_detail.html', {
            'object': node,
            'nodes': nodes
    })    