# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-26 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_gallery', '0004_auto_20191026_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
        migrations.AddField(
            model_name='video',
            name='en_name',
            field=models.CharField(db_index=True, max_length=250, null=True, verbose_name='\u0410\u043d\u0433\u043b\u0438\u0441\u0447\u0435 \u0430\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='video',
            name='kg_name',
            field=models.CharField(db_index=True, max_length=250, null=True, verbose_name='\u0412\u0438\u0434\u0435\u043e\u043d\u0443\u043d \u0430\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='video',
            name='ru_name',
            field=models.CharField(db_index=True, max_length=250, null=True, verbose_name='\u041e\u0440\u0443\u0441\u0447\u0430 \u0430\u0442\u044b'),
        ),
    ]
