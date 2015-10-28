from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
import datetime
from ckeditor.fields import RichTextField
import random
from Dajia.settings import MEDIA_PATH
# Create your models here.

# class Category(models.Model):
#     id = models.PositiveIntegerField(primary_key=True,unique=True)
#     def __str__(self):
#         return self.id.__str__()


class Category(models.Model):
    order = models.IntegerField(verbose_name='顺序',blank=False,null=False,unique=True)
    name = models.CharField(max_length=128,verbose_name='名称')
    pages = models.ManyToManyField('Page',related_name='categorys',blank=True,verbose_name='包含文章')
    def __str__(self):
        return self.name

class PageImage(models.Model):
    page = models.ForeignKey('Page',name='images')
    image = models.ImageField(MEDIA_PATH+'/%Y/%m/%d')

class Page(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128,blank=True)
    content = RichTextField(blank=True)
    slug = models.SlugField(blank=True)
    date = models.DateField(default=timezone.now,verbose_name='创建时间',editable=False)
    views = models.PositiveIntegerField(default=0)
    summary = models.CharField(max_length=200,blank=True)
    recommend = models.BooleanField(default=False,verbose_name='推荐')
    topOutDate = models.DateField(default=datetime.date.today()-datetime.timedelta(days=1),
                                  verbose_name='置顶到:')
    def get_url(self):
        return "/blog/page?id=" + str(self.id)
    def __str__(self):
        return self.title
    def isTopping(self):
        return timezone.now().date() < self.topOutDate
    def content_safe(self):
        return mark_safe(self.content)
    def save(self):
        if(self.summary == ''):
            self.summary = self.content[3:self.content.find('</p>')]
        super(Page,self).save()







