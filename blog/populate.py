__author__ = 'fengyu'

from blog.models import Page

def populate():
    for i in range(0,50):
        new = Page()
        new.title = i
        new.save()