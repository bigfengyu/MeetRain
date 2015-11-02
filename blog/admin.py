from django.contrib import admin
from blog.models import *
from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from mptt.admin import MPTTModelAdmin
from django_markdown.admin import MarkdownModelAdmin


# Register your models here.



class PageForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Page
    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if self.instance.slug != slug and slug != '' and  Page.objects.filter(slug = slug).exists():
            raise ValidationError("the slug is duplicated!")
        return slug

class CategoryForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Category
    def clean_order(self):
        ori = self.instance.order
        if (ori == 0 or ori == 1):
            return self.instance.order
        else:
            return self.cleaned_data['order']
    def clean_pages(self):
        pages = self.cleaned_data['pages']
        order = self.cleaned_data['order']
        if order == 0 and pages.count() >= 5:
            raise ValidationError("top pages can not over 5")
        return pages

class PageImageInline(admin.TabularInline):
    form = PageForm
    model = PageImage
    extra = 3
    # formset = PageImageInlineForm

class PageCategoryInline(admin.TabularInline):
    form = PageForm
    model = Category.pages.through
    extra = 1

class PageAdmin(admin.ModelAdmin):
    inlines = [PageImageInline,PageCategoryInline,]
    form = PageForm
    list_display = ['title','id','date','views','hasImage']



class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    actions = ['delete_model']
    def get_actions(self, request):
        actions = super(CategoryAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    def delete_model(self, request, set):
        try:
            for obj in set.all():
                if obj.order != 1 and obj.order != 0:
                    obj.delete()
        except AttributeError:
            if set.order != 1 and set.order != 0:
                set.delete()
    delete_model.short_description = 'Delete flow'



admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(PageImage)
admin.site.register(IndexCover)
