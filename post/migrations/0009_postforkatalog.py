# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-17 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20191016_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostForKatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438')),
                ('image', models.ImageField(upload_to='katalog/')),
                ('address', models.CharField(max_length=150, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('vid', models.CharField(max_length=150, verbose_name='\u0412\u0438\u0434 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438')),
                ('rukovoditel', models.CharField(max_length=150, verbose_name='\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c')),
                ('phone', models.CharField(max_length=150, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b')),
                ('email', models.EmailField(max_length=150, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
                ('site', models.CharField(blank=True, max_length=150, null=True, verbose_name='\u0421\u0430\u0439\u0442')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='\u0422\u0440\u0430\u043d\u0441\u043b\u0438\u0442')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.CategoryForKatalog', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0430')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Language', verbose_name='\u0422\u0438\u043b\u0438')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': '\u041f\u043e\u0441\u0442 \u0434\u043b\u044f \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430',
                'verbose_name': '\u041f\u043e\u0441\u0442 \u0434\u043b\u044f \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430',
                'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b \u0434\u043b\u044f \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430',
            },
        ),
    ]
