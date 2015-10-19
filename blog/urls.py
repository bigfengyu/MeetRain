__author__ = 'fengyu'
from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^page/$',views.pageid,name='pageid'),
                       url(r'^page/(?P<slug>\w+)/$',views.pageslug,name='pageslug')
                       )