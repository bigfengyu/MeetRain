from django.shortcuts import render
from blog.models import *
from django.http import Http404
from django.utils import timezone
from itertools import chain
# Create your views here.


# def index(request):
#     toppages = Page.objects.filter(topOutDate__gte=timezone.now).order_by('-id')[0:10]
#     dict = {}
#     if len(toppages) < 10:
#         pages = Page.objects.filter(topOutDate__lt=timezone.now).order_by('-id')[0:10-len(toppages)]
#         dict['pages']= chain(toppages,pages)
#     else:
#         dict['pages']= toppages
#     return render(request, 'blog/index/index_pages.html',dict)

def index(request):
    dict = {}
    if Category.objects.filter(order=0).exists():
        toppages = Category.objects.get(order=0).pages.all()
        if len(toppages) < 10:
            pages = Page.objects.exclude(categorys__order=0).order_by('-id')[0:10-len(toppages)]
            dict['pages']= chain(toppages,pages)
        else:
            dict['pages']= toppages
    else:
        dict['pages'] = Page.objects.order_by('-id')[0:10]
    cover = IndexCover.objects.last()
    dict['cover'] = cover
    return render(request, 'blog/index/index_pages.html',dict)

def pageid(request):
    try:
        id = request.GET['id']
        page = Page.objects.get(id=id)
    except:
        raise Http404
    return pagerender(request,page)


def pageslug(request,slug):
    page = Page.objects.get(slug=slug)
    return pagerender(request,page)

def pagerender(request,page):
    page.views += 1
    page.save()
    dict = {'page':page}
    return render(request,'blog/page.html',dict)

def get_more(request):
    pages = Page.objects.filter(id__lt=request.GET['id']).order_by('-id')[0:10]
    return render(request, 'blog/elements/pageitem.html',{'pages':pages})



def indexTags(request):
    cat = Category.objects.order_by('order')
    return render(request, 'blog/index/index_tags.html',{"category":cat})

def getMorePagesInTags(request):
    tagid = request.GET['tagid']
    pageid = request.GET['pageid']
    pages = Category.objects.get(id=tagid).pages.filter(id__lt=pageid).order_by('-id');
    return render(request, 'blog/elements/get_more_tags.html',{"pages":pages})



