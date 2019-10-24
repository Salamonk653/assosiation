# -*- coding: utf-8 -*-
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe


class Language(models.Model):
    class Meta:
        db_table = u'Тил'
        verbose_name = u'Тил'
        verbose_name_plural = u'Тилдер'
        ordering = [u'-id']

    name = models.CharField(verbose_name=u'Аты', max_length=80, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class GlavCategory(models.Model):
    class Meta:
        db_table = u'Главная категория'
        verbose_name_plural = u'Главные категории'
        verbose_name = u'Главная категория'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Аты', max_length=150)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    style = models.CharField(verbose_name=u'Добавить класс', max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    class Meta:
        db_table = u'Category'
        verbose_name = u'Категория'
        verbose_name_plural = u'Категориялар'
        ordering = [u'-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    glavcategory = models.ForeignKey(GlavCategory, verbose_name=u'Главная категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Аты', max_length=80, blank=True, null=True, default=None)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse(u'category_detail', kwargs={u'slug': self.slug})

    def __unicode__(self):
        return self.name


class New(models.Model):
    class Meta:
        verbose_name_plural = u'Жаңылыктар'
        verbose_name = u'Жаңылык'
        ordering = [u'-id']

    category = models.ForeignKey(Category, verbose_name=u'Категория',
                                 default=1, on_delete=models.CASCADE,
                                 blank=True, null=True)
    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Макаланын аталышы', db_index=True, max_length=255)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
    image = models.ImageField(verbose_name=u'Сүрөт', upload_to=u'news/', blank=True, null=True)
    text = RichTextUploadingField(verbose_name=u'Маалымат')
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    user_rection = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    created = models.DateTimeField(verbose_name=u'Дата', default=timezone.now)
    author = models.CharField(verbose_name=u'Макаланын автору', blank=True, null=True, max_length=200)
    start_time = models.DateTimeField(verbose_name=u'Начало', blank=True, null=True)
    end_time = models.DateTimeField(verbose_name=u'Конец', blank=True, null=True)
    organizator = models.CharField(verbose_name=u'Организатор', max_length=150, blank=True, null=True)
    mesto = models.CharField(verbose_name=u'Место проведения', max_length=150, blank=True, null=True)
    protsent = models.IntegerField(verbose_name=u'Процент проекта', blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse(u'ru_article_detail', kwargs={u'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = u'Сүрөт'

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(New, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.name


class GlavSlider(models.Model):
    class Meta:
        verbose_name_plural = u'Слайдер'
        verbose_name = u'Слайдер'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Аты', max_length=200)
    text = models.TextField(verbose_name=u'Маалымат')
    image = models.ImageField(verbose_name=u'Фото для слайдера', upload_to=u'slider/')

    def __unicode__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = u'Сүрөт'


class OFonde(models.Model):
    class Meta:
        verbose_name_plural = u'Ассоциация жөнүндө'
        verbose_name = u'Ассоциация жөнүндө'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    adres = models.CharField(verbose_name=u'Дарек', max_length=200, db_index=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=150, db_index=True)
    email = models.EmailField(verbose_name=u'Емейл')
    karta = models.CharField(verbose_name=u'Карта', max_length=400)
    facebook = models.CharField(verbose_name=u'Фейсбук', max_length=250, blank=True, null=True)
    instagram = models.CharField(verbose_name=u'Инстаграм', max_length=250, blank=True, null=True)
    youtube = models.CharField(verbose_name=u'Ютуб', max_length=250, blank=True, null=True)

    def __unicode__(self):
        return str(self.id)


class Fondjonundo(models.Model):
    class Meta:
        db_table = u'Ассоциация'
        verbose_name_plural = u'Ассоциациянын ачыктамасы'
        verbose_name = u'Ассоциациянын ачыктамасы'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Аты', max_length=100)
    text = RichTextUploadingField(verbose_name=u'Багыттар', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Chlen_Partner(models.Model):
    class Meta:
        verbose_name_plural = u'Члены и партнеры'
        verbose_name = u'Члены и партнеры'
        ordering = ['-id']

    category = models.ForeignKey(Category, verbose_name=u'Категория', default=1, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=u'Сүрөт', upload_to=u'chlleny/')

    def __unicode__(self):
        return str(self.id)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = u'Сүрөт'


class GlavCategoryForKatalog(models.Model):
        class Meta:
            db_table = u'Главная категория для каталога'
            verbose_name_plural = u'Главные категории для каталога'
            verbose_name = u'Главная категория для каталога'
            ordering = ['-id']

        language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
        name = models.CharField(verbose_name=u'Аты', max_length=150)
        slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)
        style = models.CharField(verbose_name=u'Добавить класс', max_length=200, blank=True, null=True)

        def __unicode__(self):
            return self.name


class CategoryForKatalog(models.Model):
        class Meta:
            db_table = u'Категория для каталога'
            verbose_name_plural = u'Категории для каталога'
            verbose_name = u'Категория для каталога'
            ordering = ['-id']

        language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
        glavcategory = models.ForeignKey(GlavCategoryForKatalog, verbose_name=u'Главная категория для каталога',
                                         on_delete=models.CASCADE)
        name = models.CharField(verbose_name=u'Аты', max_length=150)
        slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)

        def __unicode__(self):
            return self.name


class PostForKatalog(models.Model):
    class Meta:
        db_table = u'Пост для каталога'
        verbose_name_plural = u'Посты для каталога'
        verbose_name = u'Пост для каталога'
        ordering = ['-id']

    language = models.ForeignKey(Language, verbose_name=u'Тили', on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryForKatalog, verbose_name=u'Категория для поста',
                                     on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Наименование организации', max_length=150)
    image = models.ImageField(upload_to=u'katalog/')
    address = models.CharField(verbose_name=u'Место нахождения', max_length=150)
    vid = models.CharField(verbose_name=u'Вид деятельности', max_length=150)
    rukovoditel = models.CharField(verbose_name=u'Руководитель', max_length=150)
    phone = models.CharField(verbose_name=u'Контакты', max_length=150)
    email = models.EmailField(verbose_name=u'Почта', max_length=150)
    site = models.CharField(verbose_name=u'Сайт', max_length=150, blank=True, null=True)
    slug = models.CharField(verbose_name=u'Транслит', max_length=200, blank=True)

    def __unicode__(self):
        return self.name