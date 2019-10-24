# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-13 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0006_new_protsent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='\u0410\u043b\u044c\u0431\u043e\u043c\u0434\u0443\u043d \u0430\u0442\u044b')),
                ('ru_name', models.CharField(db_index=True, max_length=250, verbose_name='\u041e\u0440\u0443\u0441\u0447\u0430 \u0430\u0442\u044b')),
                ('oblojka', models.ImageField(upload_to=b'album/oblojka/', verbose_name='\u0410\u043b\u044c\u0431\u043e\u043c\u0434\u0443\u043d \u043e\u0431\u043b\u043e\u0436\u043a\u0430\u0441\u044b')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='\u0422\u0440\u0430\u043d\u0441\u043b\u0438\u0442')),
                ('is_public', models.BooleanField(default=True, verbose_name='\u041a\u04e9\u0440\u04af\u043d\u0441\u04af\u043d')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u0434\u043e\u0440',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'gallery/', verbose_name='\u0421\u04af\u0440\u04e9\u0442')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u041c\u0430\u0430\u043b\u044b\u043c\u0430\u0442')),
                ('ru_description', models.TextField(blank=True, null=True, verbose_name='\u041e\u0440\u0443\u0441\u0447\u0430')),
                ('is_public', models.BooleanField(default=True, verbose_name='\u041a\u04e9\u0440\u04af\u043d\u0441\u04af\u043d')),
                ('album', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='media_gallery.Album', verbose_name='\u0410\u043b\u0431\u043e\u043c')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0421\u04af\u0440\u04e9\u0442',
                'verbose_name_plural': '\u0421\u04af\u0440\u04e9\u0442\u0442\u04e9\u0440',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='\u0412\u0438\u0434\u0435\u043e\u043d\u0443\u043d \u0430\u0442\u044b')),
                ('ru_name', models.CharField(db_index=True, max_length=250, verbose_name='\u041e\u0440\u0443\u0441\u0447\u0430 \u0430\u0442\u044b')),
                ('oblojka', models.ImageField(upload_to=b'video/', verbose_name='\u0412\u0438\u0434\u0435\u043e\u043d\u0443\u043d \u043e\u0431\u0434\u043e\u0436\u043a\u0430\u0441\u044b')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='\u0422\u0440\u0430\u043d\u0441\u043b\u0438\u0442')),
                ('video_url', models.CharField(blank=True, max_length=200, verbose_name='\u0412\u0438\u0434\u0435\u043e\u043d\u0443\u043d \u0441\u0441\u044b\u043b\u043a\u0430\u0441\u044b')),
                ('is_public', models.BooleanField(default=True, verbose_name='\u041a\u04e9\u0440\u04af\u043d\u0441\u04af\u043d')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Language', verbose_name='\u0422\u0438\u043b\u0438')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e\u043b\u043e\u0440',
            },
        ),
    ]
