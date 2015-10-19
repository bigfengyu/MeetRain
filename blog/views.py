from django.shortcuts import render
from blog.models import Page
from django.http import Http404
# Create your views here.


def index(request):
    return render(request,'blog/index.html',{'pages':Page.objects.order_by('-id')})

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



# def getmore(request,start,lenth):

