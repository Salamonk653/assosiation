# -*- coding: utf-8 -*-
# Create your models here.
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from django.views.generic import *

from media_gallery.models import *
from post.en_views import Navbar, Search


class GalleeryList(ListView, Navbar):
    model = Album
    template_name = 'en/album_list.html'
    queryset = Album.objects.filter(is_public=True).order_by('-id')
    context_object_name = 'albums'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super(GalleeryList, self).get_context_data(**kwargs)
        context['h2'] = 'Association photo gallery'
        return context


class ImageList(Search):

    def get(self, request, slug):
        album = Album.objects.get(slug=slug)
        images = album.image_set.filter(is_public=True).order_by('-id')
        paginator = Paginator(images, 20)
        page_number = request.GET.get('page', 1)
        page = paginator.page(page_number)
        self.context['album'] = album
        self.context['page_obj'] = page
        self.context['is_paginated'] = page.has_other_pages()
        self.context['h2'] = album.en_name
        return render(request, 'en/image_list.html', self.context)


class VideoList(ListView, Navbar):
    model = Video
    template_name = 'en/video_list.html'
    paginate_by = 20
    queryset = Video.objects.filter(is_public=True).order_by('-id')
    context_object_name = 'videos'

    def get_context_data(self, *args, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context['h2'] = 'association video portal'
        return context
