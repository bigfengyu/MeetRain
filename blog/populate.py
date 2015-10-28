__author__ = 'fengyu'

from blog.models import Page
import datetime
def populate():
    for i in range(0,50):
        new = Page()
        new.title = i
        new.save()