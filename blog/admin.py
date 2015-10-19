from django.contrib import admin
from blog.models import Page
from django import forms


# Register your models here.




class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','date','views']


admin.site.register(Page,PostAdmin)