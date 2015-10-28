from django.contrib import admin
from blog.models import *
from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from mptt.admin import MPTTModelAdmin
from django_markdown.admin import MarkdownModelAdmin


# Register your models here.



class AdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Page
    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if slug != '' and  Page.objects.filter(slug = slug).exists():
            raise ValidationError("the slug is duplicated!")
        return slug



class PageImageInline(admin.TabularInline):
    form = AdminForm
    model = PageImage
    extra = 3
    # formset = PageImageInlineForm

class PageCategoryInline(admin.TabularInline):
    form = AdminForm
    model = Category.pages.through
    extra = 1

class PageAdmin(admin.ModelAdmin):
    inlines = [PageImageInline,PageCategoryInline,]
    form = AdminForm
    list_display = ['title','id','date','views',]

# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [PageCategoryInline,]

admin.site.register(Page,PageAdmin)
admin.site.register(Category)
admin.site.register(PageImage)
