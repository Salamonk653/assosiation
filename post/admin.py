# -*- coding: utf-8 -*-
# Create your models here.
from django.contrib import admin

# Register your models here.
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GlavCategoryAdmin(admin.ModelAdmin):
    list_filter = ('language',)
    list_display = ['name', 'language']
    prepopulated_fields = {'slug': ('name',)}


class ChlenAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ['image_tag', 'category']
    readonly_fields = ['image_tag']


class NewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'likes', 'dislikes', 'is_public']
    ordering = ['category']
    readonly_fields = ['image_tag']
    search_fields = ('name', 'text')
    list_filter = ('category', 'is_public', 'language')
    list_per_page = 20
    # list_display_links = 'name'


class GlavCategoryAdminForCatalog(admin.ModelAdmin):
    list_filter = ('language',)
    list_display = ['name', 'language']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdminForCatalog(admin.ModelAdmin):
    list_filter = ('language',)
    list_display = ['name', 'language']
    prepopulated_fields = {'slug': ('name',)}


class PostAdminForCatalog(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category']
    ordering = ['category']
    search_fields = ('name', 'text')
    list_filter = ('category', 'language')
    list_per_page = 20


admin.site.register(OFonde)
admin.site.register(GlavSlider)
admin.site.register(GlavCategory, GlavCategoryAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Fondjonundo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language)
admin.site.register(Chlen_Partner, ChlenAdmin)
admin.site.register(GlavCategoryForKatalog, GlavCategoryAdminForCatalog)
admin.site.register(CategoryForKatalog, CategoryAdminForCatalog)
admin.site.register(PostForKatalog, PostAdminForCatalog)
