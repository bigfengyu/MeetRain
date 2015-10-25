from django.shortcuts import render
from blog.models import *
from django.http import Http404
# Create your views here.


def index(request):
    pages = Page.objects.order_by('-id')[0:10]
    return render(request, 'blog/index_pages.html',{'pages':pages})

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
    return render(request, 'blog/content.html',{'pages':pages})



def indexTags(request):
    cat = Category.objects.order_by('id')
    return render(request,'blog/index_tags.html',{"category":cat})

def getMorePagesInTags(request):
    tagid = request.GET['tagid']
    pageid = request.GET['pageid']
    pages = Category.objects.get(id=tagid).pages.filter(id__lt=pageid).order_by('-id');
    return render(request,'blog/get_more_tags.html',{"pages":pages})



