from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django_markdown.models import MarkdownField
def orderfill():
    last = Category.objects.all().aggregate(models.Max('order'))['order__max']
    if last is None:
        return 0
    return last + 1

class Category(models.Model):
    order = models.IntegerField(verbose_name='顺序',blank=False,null=False,unique=True,
                                default=orderfill)
    name = models.CharField(max_length=128,verbose_name='名称')
    pages = models.ManyToManyField('Page',related_name='categorys',blank=True,verbose_name='包含文章')
    normalOrder = models.BooleanField(blank=False,null=False)
    def __str__(self):
        return self.name



class PageImage(models.Model):
    page = models.ForeignKey('Page',related_name='images',verbose_name='属于文章')
    image = models.ImageField(upload_to="media/%y/%m/%d")


class Page(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128,blank=True)
    content = MarkdownField(blank=True)
    slug = models.SlugField(blank=True,max_length=255)
    date = models.DateField(default=timezone.now,verbose_name='创建时间',editable=False)
    views = models.PositiveIntegerField(default=0)
    summary = models.CharField(max_length=200,blank=False)
    def hasImage(self):
        return self.images.exists()
    def getCoverImageUrl(self):
        if not self.hasImage():
            return '/static/img/meetrain.png'
        else:
            return self.images.first().image.url
    def get_url(self):
        return "/blog/page?id=" + str(self.id)
    def __str__(self):
        return self.title
    def isTopping(self):
        return self.categorys.filter(order=0).exists()
    def isRec(self):
        return self.categorys.filter(order=1).exists()
    def content_safe(self):
        return self.content
    def save(self):
        super(Page,self).save()

class IndexCover(models.Model):
    page = models.OneToOneField('Page')
    class Meta:
        verbose_name = "Cover"
    def imageurl(self):
        return self.page.getCoverImageUrl()
    def __str__(self):
        return self.page.title





