__author__ = 'fengyu'
from django.conf.urls import patterns, url
from blog import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^page/$',views.pageid,name='pageid'),
                       url(r'^about/$',views.indexAbout,name='indexabout'),
                       url(r'^page/(?P<slug>\w+)/$',views.pageslug,name='pageslug'),
                       url(r'^get_more/',views.get_more,name='get_more'),
                       url(r'^tags/$',views.indexTags,name='indextags'),
                       url(r'^tags/get_more',views.getMorePagesInTags,name='getMorePagesInTags'),
                       )