# -*- coding: utf-8 -*-
# Create your models here.
from django import template
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.views.generic.base import ContextMixin

from post.forms import ContactForm
from .models import *


class Navbar(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super(Navbar, self).get_context_data(**kwargs)
        merop = GlavCategory.objects.get(name__icontains=u'Наши проекты')
        context['navbar'] = merop.category_set.filter(language__name__icontains=u'ru')
        context['anonsy'] = Category.objects.get(name__icontains=u'Анонсы')
        context['articles_4'] = New.objects.filter(language__name__icontains='ru',
                                                   category__name__icontains=u'Жаңылыктар', is_public=True).order_by(
            '-id')[:5]
        context['form'] = ContactForm()
        context['assosiations'] = OFonde.objects.filter(language__name__icontains='ru').first()
        return context


class News(ListView, Navbar):
    model = New
    template_name = u'ru/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['news'] = New.objects.filter(category__name__iexact=u'Жаңылыктар', language__name__icontains=u'ru',
                                             is_public=True).order_by('-id')[:3]
        context['merop'] = New.objects.filter(category__name__iexact=u'Анонсы', language__name__icontains=u'ru',
                                              is_public=True).order_by('-id')[:3]
        context['projects'] = New.objects.filter(category__glavcategory__name__icontains=u'Наши проекты',
                                                 language__name__icontains=u'ru', is_public=True).order_by('-id')[:8]
        index = []
        for i in range(1, context['projects'].count() + 1):
            index.append(i)
        context['index'] = index
        context['sliders'] = GlavSlider.objects.filter(language__name__icontains=u'ru')
        context['chlens'] = Chlen_Partner.objects.filter(category__name__iexact=u'Члены')
        context['partners'] = Chlen_Partner.objects.filter(category__name__iexact=u'Партнеры')
        return context


class Podrobnee(TemplateView, Navbar):
    template_name = 'ru/podrobnee.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Podrobnee, self).get_context_data(**kwargs)
        context['h2'] = 'Что дает членство в МАПЭФ?'
        return context


class NewsList(ListView, Navbar):
    model = New
    template_name = u'ru/novosti.html'
    queryset = New.objects.filter(category__name__icontains=u'Жаңылыктар', language__name__icontains='ru').order_by(
        '-id')
    paginate_by = 6
    context_object_name = u'category'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['h2'] = u'Новости'
        return context


class AnonsyList(ListView, Navbar):
    model = New
    template_name = u'ru/anonsy.html'
    queryset = New.objects.filter(category__name__icontains=u'Анонсы', language__name__icontains='ru').order_by('-id')
    paginate_by = 6
    context_object_name = u'category'

    def get_context_data(self, *args, **kwargs):
        context = super(AnonsyList, self).get_context_data(**kwargs)
        context['h2'] = 'Анонсы'
        return context


class AnonsyDetail(DetailView, Navbar):
    model = New
    template_name = 'ru/anonsy_detail.html'
    category = Category

    def get_context_data(self, *args, **kwargs):
        context = super(AnonsyDetail, self).get_context_data(**kwargs)
        context['articles'] = self.model.objects.filter(language__name__icontains='ru',
                                                        category__name__icontains=u'Жаңылыктар',
                                                        is_public=True).order_by('-id')[:15]
        context['projects'] = New.objects.filter(category__glavcategory__name__icontains=u'Наши проекты',
                                                 language__name__icontains=u'ru', is_public=True).order_by('-id')[:15]
        context['article'] = self.get_object()
        context['h2'] = self.get_object()
        return context


class Projects(ListView, Navbar):
    model = New
    queryset = New.objects.filter(category__glavcategory__name__icontains=u'Наши проекты',
                                  language__name__icontains=u'ru', is_public=True).order_by('-id')
    context_object_name = u'projects'
    paginate_by = 6
    template_name = 'ru/proejects.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Projects, self).get_context_data(**kwargs)
        context['h2'] = u'Наши проекты'
        return context


class ProjectList(DetailView, Navbar):
    model = Category
    template_name = 'ru/nashi_proecty.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        category = self.get_object()
        context['category'] = category.new_set.filter(language__name__icontains='ru').order_by('-id')
        context['h2'] = self.get_object()
        return context


class ArticleDetail(DetailView, Navbar):
    model = New
    template_name = 'ru/novosti_detail.html'
    category = Category

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['articles'] = self.model.objects.filter(language__name__icontains='ru',
                                                        category__name__icontains=u'Жаңылыктар',
                                                        is_public=True).order_by('-id')[:15]
        context['projects'] = New.objects.filter(category__glavcategory__name__icontains=u'Наши проекты',
                                                 language__name__icontains=u'ru', is_public=True).order_by('-id')[:8]
        context['article'] = self.get_object()
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['h2'] = self.get_object()
        return context


class Chlenstvo(TemplateView, Navbar):
    template_name = 'ru/chlenstvo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Chlenstvo, self).get_context_data(**kwargs)
        context['h2'] = 'Членство'
        return context


class Contacts(TemplateView, Navbar):
    template_name = 'ru/contacts.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Contacts, self).get_context_data(**kwargs)
        context['h2'] = 'Наши контакты'
        return context


class Onas(TemplateView, Navbar):
    template_name = 'ru/onas.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Onas, self).get_context_data(**kwargs)
        context['h2'] = 'О НАС'
        context['fond'] = Fondjonundo.objects.filter(language__name__icontains='ru').order_by('id')
        return context


class Search(View):
    template_name = 'ru/search.html'
    merop = GlavCategory.objects.get(name__icontains=u'Наши проекты')
    context = {'assosiations': OFonde.objects.filter(language__name__icontains='ru').first(),
               'navbar': merop.category_set.filter(language__name__icontains=u'ru'),
               'anonsy': Category.objects.get(name__icontains=u'Анонсы'),
               'articles_4': New.objects.filter(language__name__icontains='ru', category__name__icontains=u'Жаңылыктар',
                                                is_public=True).order_by('-id')[:5],
               'form': ContactForm(),
               }

    # context = {}

    def get(self, request):
        self.context['h2'] = 'ПОИСК'
        self.context['text'] = 'Мы искали, но у вы!'

        q = request.GET.get('q')
        if q:
            self.context['posts'] = New.objects.filter(name__icontains=q, language__name__icontains='ru')
        else:
            self.context['posts'] = ''
        # return context
        return render(request, self.template_name, self.context)


def contact_form(request):
    sent = False
    mailto = ['salamonk653@gmail.com']
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = u'МАПЭФ - Новое письмо от {}'.format(name)
            message = u'Емайл: {}. Телефон: {}'.format(email, phone)
            sent = True
            try:
                send_mail(subject, message, 'sulaiman.97_kg@mail.ru', mailto)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            return redirect(u'ru_news_list')
    else:
        form = ContactForm()
    return render(request, 'ru/index.html', {'forms': form, 'sent': sent})


class Katalog(TemplateView, Navbar):
    template_name = 'ru/katolog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Katalog, self).get_context_data(**kwargs)
        context['h2'] = 'КАТАЛОГ'
        glavnyi = GlavCategoryForKatalog.objects.filter(language__name__icontains=u'ru')
        context['glavnyi'] = glavnyi
        return context


class KatalogDetail(Search):
    template_name = 'ru/katolog_detail.html'

    def get(self, request, slug):
        glavnyi = PostForKatalog.objects.filter(category__glavcategory__slug__icontains=slug,
                                                language__name__icontains=u'ru') or PostForKatalog.objects.filter(
            category__slug__icontains=slug,
            language__name__icontains=u'ru')
        paginator = Paginator(glavnyi, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.page(page_number)
        self.context['page_obj'] = page
        self.context['is_paginated'] = page.has_other_pages()
        self.context['h2'] = 'КАТАЛОГ'
        self.context['glavnyi'] = glavnyi
        self.context['test'] = ''''''
        return render(request, self.template_name, self.context)
