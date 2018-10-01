from django.shortcuts import render, render_to_response
from django.db.models import Q
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

# Create your views here.
from .models import MPTTArticle, Course

def course_list(request):
    object_list= Course.objects.all(is_superuser=request.user.is_superuser)
     
    return render(request, 'course_list.html', {'object_list': object_list})

def course_detail(request, pk):
    node= Course.objects.get(pk=pk)

    article_root = MPTTArticle.objects.root(is_superuser=request.user.is_superuser).filter(course=node)
     
    return render(request, 'course_detail.html', {
            'object': node,
            'article_root':article_root,
    })    


def article_list(request):
    # nodes= MPTTArticle.objects.root_nodes()

    # nodes= MPTTArticle.objects.filter(parent=None)
    # if not request.user.is_superuser:
    #     nodes = nodes.filter(active=True)
    nodes= MPTTArticle.objects.root(is_superuser=request.user.is_superuser)

    return render(request, 'article_list.html', {'nodes': nodes})


def article_detail(request, pk1, pk):
    try:
        articles = MPTTArticle.objects.all(is_superuser=request.user.is_superuser).filter(course__id=pk1)
        # if not request.user.is_superuser:
        #     articles = articles.filter(active=True)
    except:
        articles = None

    if articles:
        node= articles.get(pk=pk)
        nodes= articles

    # first get the related HitCount object for your model object
    hit_count = HitCount.objects.get_for_object(node)

    # next, you can attempt to count a hit and get the response
    # you need to pass it the request object as well
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    # print hit_count_response._asdict()

    # your response could look like this:
    # UpdateHitCountResponse(hit_counted=True, hit_message='Hit counted: session key')
    # UpdateHitCountResponse(hit_counted=False, hit_message='Not counted: session key has active hit')

    context = {
            'object': node,
            'nodes': nodes,
    }

    context.update(hit_count_response._asdict())
     
    return render(request, 'article_detail.html', {
            'object': node,
            'nodes': nodes,
    })

def article_search_list(request):

    q = request.GET.get('q', None)
    # print q
    if q:
        nodes= MPTTArticle.objects.all(is_superuser=request.user.is_superuser).filter(Q(title__icontains=q) | Q(content__icontains=q))
    else:
        nodes = MPTTArticle.objects.all(is_superuser=request.user.is_superuser)

    return render(request, 'article_search_list.html', 
        {'nodes': nodes, 'q':q})
    