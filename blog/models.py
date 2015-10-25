from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
import datetime
from ckeditor.fields import RichTextField
import random
from django_markdown.models import MarkdownField

# Create your models here.

# class Category(models.Model):
#     id = models.PositiveIntegerField(primary_key=True,unique=True)
#     def __str__(self):
#         return self.id.__str__()

class Test(models.Model):
    text = MarkdownField()


class Category(models.Model):
    name = models.CharField(max_length=128,verbose_name='名称')
    pages = models.ManyToManyField('Page',related_name='categorys',blank=True,verbose_name='包含文章')
    def __str__(self):
        return self.name

class PageImage(models.Model):
    page = models.ForeignKey('Page')
    image = models.ImageField(upload_to='%Y/%m/%d')

class Page(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128,blank=True)
    content = RichTextField(blank=True)
    slug = models.SlugField(blank=True)
    date = models.DateField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    summary = models.CharField(max_length=200,blank=True)
    recommend = models.BooleanField(default=False)
    def get_url(self):
        return "/blog/page?id=" + str(self.id)
    def __str__(self):
        return self.title
    def content_safe(self):
        return mark_safe(self.content)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if(self.summary == ''):
            print("in")
            self.summary = self.content[3:self.content.find('</p>')]
        super(Page,self).save()



