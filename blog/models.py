from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
import datetime
from ckeditor.fields import RichTextField
import random
from Dajia.settings import MEDIA_PATH
from django_markdown.models import MarkdownField
import os
from django.core.exceptions import ValidationError
# Create your models here.

# class Category(models.Model):
#     id = models.PositiveIntegerField(primary_key=True,unique=True)
#     def __str__(self):
#         return self.id.__str__()

today = timezone.datetime.now()

class Category(models.Model):
    order = models.IntegerField(verbose_name='顺序',blank=False,null=False,unique=True)
    name = models.CharField(max_length=128,verbose_name='名称')
    pages = models.ManyToManyField('Page',related_name='categorys',blank=True,verbose_name='包含文章')
    def __str__(self):
        return self.name
    # def delete(self, using=None):
    #     if self.order == 0 or self.order == 1:
    #         raise ValidationError("cannot delete top or rec record")
    #     else:
    #         super(Category,self).delete()


class PageImage(models.Model):
    page = models.ForeignKey('Page',related_name='images',verbose_name='属于文章')
    image = models.ImageField(upload_to="%y/%m/%d")


class Page(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128,blank=True)
    content = MarkdownField()
    slug = models.SlugField(blank=True)
    date = models.DateField(default=timezone.now,verbose_name='创建时间',editable=False)
    views = models.PositiveIntegerField(default=0)
    summary = models.CharField(max_length=200,blank=True)
    def get_url(self):
        return "/blog/page?id=" + str(self.id)
    def __str__(self):
        return self.title
    def isTopping(self):
        return self.categorys.filter(order=0).exists()
    def isRec(self):
        return self.categorys.filter(order=1).exists()
    def content_safe(self):
        return mark_safe(self.content)
    def save(self):
        if(self.summary == ''):
            self.summary = self.content[3:self.content.find('</p>')]
        super(Page,self).save()

class IndexCover(models.Model):
    page = models.OneToOneField('Page')
    def imageurl(self):
        return self.page.images.first().image.url
    def __str__(self):
        return self.page.title





