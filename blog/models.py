from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
import uuid
import datetime
from ckeditor.fields import RichTextField
import random
# Create your models here.

# class Category(models.Model):
#     id = models.PositiveIntegerField(primary_key=True,unique=True)
#     def __str__(self):
#         return self.id.__str__()

class Page(models.Model):
    # category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128,blank=True)
    content = RichTextField(blank=True)
    slug = models.SlugField(unique=True,default=timezone.now().__format__('%y%m%d%H%M')+str(uuid.uuid1()))
    date = models.DateField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    summary = models.CharField(max_length=200,blank=True)
    recommend = models.BooleanField(default=False)
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


