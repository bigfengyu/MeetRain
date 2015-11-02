__author__ = 'fengyu'

from blog.models import *
import datetime

names = ['置顶','忒贱','叫我序员就行','见好就收','俗家奇遇']
for i in range(0,5):
    try:
        item = Category(order=i,name=names[i],normalOrder=False)
        item.save()
    except:
        pass
for i in range(0,50):
    new = Page()
    new.title = i
    new.save()

