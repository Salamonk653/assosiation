# -*- coding: utf-8 -*-
# Create your models here.
from django.conf.urls import url

from .ru_views import *

urlpatterns = [
    url(r'^$', News.as_view(), name='ru_news_list'),
    url(r'^contact/form/$', contact_form, name='ru_contact_form'),
    url(r'^category/news/$', NewsList.as_view(), name='ru_category'),
    url(r'^category/anonsy/$', AnonsyList.as_view(), name='ru_anonsy'),
    url(r'^category/projects/$', Projects.as_view(), name='ru_projects'),
    url(r'^anonsy/(?P<slug>[\w-]+)/$', AnonsyDetail.as_view(), name='ru_anonsy_detail'),
    url(r'^category/contacts/$', Contacts.as_view(), name='ru_contacts'),
    url(r'^category/katalog/$', Katalog.as_view(), name='ru_katalog'),
    url(r'^category/katalog/(?P<slug>[\w-]+)/$', KatalogDetail.as_view(), name='ru_katalog_detail'),
    url(r'^category/chlenstvo/$', Chlenstvo.as_view(), name='ru_chlenstvo'),
    url(r'^category/onas/$', Onas.as_view(), name='ru_onas'),
    url(r'^category/(?P<slug>[\w-]+)/$', ProjectList.as_view(), name='ru_category_detail'),
    url(r'^article/(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='ru_article_detail'),
    url(r'^search/$', Search.as_view(), name='ru_search'),
    url(r'^podrobnee/$', Podrobnee.as_view(), name='ru_podrobnee'),
]
