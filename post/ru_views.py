# -*- coding: utf-8 -*-
# Create your models here.
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.views.generic.base import ContextMixin

from AssosiationDjango import local_settings
from post.forms import ContactForm
from .models import *


class Navbar(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super(Navbar, self).get_context_data(**kwargs)
        merop = get_object_or_404(GlavCategory, name__icontains=u'Наши проекты', language__name__icontains=u'ru')
        context['navbar'] = merop.category_set.filter(language__name__icontains=u'ru')
        context['anonsy'] = get_object_or_404(Category, name__icontains=u'Анонсы', language__name__icontains=u'ru')
        context['articles_4'] = New.objects.filter(language__name__icontains='ru', is_public=True).order_by('-id')[:5]
        context['form'] = ContactForm()
        return context


class News(ListView, Navbar):
    model = New
    template_name = u'ru/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['news'] = New.objects.filter(category__name__iexact=u'Жаңылыктар', language__name__icontains=u'ru',
                                             is_public=True).order_by('-id')[:4]
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
        context['articles'] = self.model.objects.filter(language__name__icontains='ru', is_public=True).order_by('-id')[
                              :15]
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
        context['articles'] = self.model.objects.filter(language__name__icontains='ru', is_public=True).order_by('-id')[
                              :15]
        context['article'] = self.get_object()
        context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
        context['h2'] = self.get_object()
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


class UserReactionView(View):
    template_name = 'ru/new_list_detail.html'

    def get(self, request, *args, **kwargs):
        article_id = self.request.GET.get('article_id')
        article = New.objects.get(id=article_id)
        like = self.request.GET.get('like')
        dislike = self.request.GET.get('dislike')
        if like and (request.user not in article.user_rection.all()):
            article.likes += 1
            article.user_rection.add(request.user)
            article.save()
        if dislike and (request.user not in article.user_rection.all()):
            article.dislikes += 1
            article.user_rection.add(request.user)
            article.save()
        dannyi = {
            'likes': article.likes,
            'dislikes': article.dislikes
        }
        return JsonResponse(dannyi)


from django.shortcuts import render


# from .documents import PostDocument


def search(request):
    context = {}
    q = request.GET.get('q')

    if q:
        # context['posts'] = PostDocument.search().query("match", name=q)
        context['posts'] = New.objects.filter(name__icontains=q, language__name__icontains='ru')
    else:
        context['posts'] = ''

    context['ofonde'] = OFonde.objects.filter(language__name__icontains='ru').first()
    return render(request, 'ru/search/search.html', context)


def contact_form(request):
    sent = False
    mailfrom = local_settings.EMAIL_HOST_USER
    mailto = ['salamonk653@gmail.com']
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = u'МАПЭФ - Новое письмо от {}'.format(name)
            # subject = u'МАПЭФ - Новое письмо от {}' + name
            message = u'Емайл: {}. Телефон: {}'.format(email, phone)
            # send_mail(subject, message, mailfrom, mailto)
            sent = True
            try:
                send_mail(subject, message, 'sulaiman.97_kg@mail.ru', mailto)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            return redirect(u'ru_news_list')
    else:
        form = ContactForm()
    return render(request, 'ru/index.html', {'forms': form, 'sent': sent})

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     # Если форма заполнена корректно, сохраняем все введённые пользователем значения
    #     if form.is_valid():
    #         subject = form.cleaned_data['name']
    #         sender = form.cleaned_data['email']
    #         message = form.cleaned_data['phone']
    #
    #         text = 'Salam ' + sender + ' phone ' + message
    #         recepients = ['salamonk653@gmail.com']
    #         # Если пользователь захотел получить копию себе, добавляем его в список получателей
    #         try:
    #             send_mail(subject, text, 'sulaiman.97_kg@mail.ru', recepients)
    #         except BadHeaderError:  # Защита от уязвимости
    #             return HttpResponse('Invalid header found')
    #         # Переходим на другую страницу, если сообщение отправлено
    #         return HttpResponseRedirect('/')
    #
    # else:
    #     form = ContactForm()
    #     # Выводим форму в шаблон
    # return render(request, 'ru/index.html', {'form': form})
