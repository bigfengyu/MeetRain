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





def indexTags(request):
    cat = Category.objects.filter(order__gt=0).order_by('order')
    return render(request, 'blog/index/index_tags.html',{"category":cat})

def getMorePagesInTags(request):
    tagid = request.GET['tagid']
    pageid = request.GET['pageid']
    tagitem = Category.objects.get(id=tagid)
    if tagitem.normalOrder:
        pages = tagitem.pages.filter(id__gt=pageid).order_by('id')
    else:
        pages = tagitem.pages.filter(id__lt=pageid).order_by('-id')
    return render(request, 'blog/elements/get_more_tags.html',{'pages':pages})

def get_more(request):
    pages = Page.objects.filter(id__lt=request.GET['id']).order_by('-id').exclude(categorys__order=0)[0:10]
    return render(request, 'blog/elements/pageitem.html',{'pages':pages})

def indexAbout(request):
    return render(request,'blog/index/index_about.html')


