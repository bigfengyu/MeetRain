__author__ = 'fengyu'

from blog.models import *
import datetime
top = Category(order=0,name='置顶')
rec = Category(order=1,name='推荐')
top.save()
rec.save()
for i in range(0,50):
    new = Page()
    new.title = i
    new.save()

