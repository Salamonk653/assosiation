# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-08 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_chlen_partner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fondjonundo',
            options={'ordering': ['-id'], 'verbose_name': '\u0410\u0441\u0441\u043e\u0446\u0438\u0430\u0446\u0438\u044f\u043d\u044b\u043d \u0430\u0447\u044b\u043a\u0442\u0430\u043c\u0430\u0441\u044b', 'verbose_name_plural': '\u0410\u0441\u0441\u043e\u0446\u0438\u0430\u0446\u0438\u044f\u043d\u044b\u043d \u0430\u0447\u044b\u043a\u0442\u0430\u043c\u0430\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='ofonde',
            options={'ordering': ['-id'], 'verbose_name': '\u0410\u0441\u0441\u043e\u0446\u0438\u0430\u0446\u0438\u044f \u0436\u04e9\u043d\u04af\u043d\u0434\u04e9', 'verbose_name_plural': '\u0410\u0441\u0441\u043e\u0446\u0438\u0430\u0446\u0438\u044f \u0436\u04e9\u043d\u04af\u043d\u0434\u04e9'},
        ),
        migrations.RemoveField(
            model_name='ofonde',
            name='name',
        ),
        migrations.AlterModelTable(
            name='fondjonundo',
            table='\u0410\u0441\u0441\u043e\u0446\u0438\u0430\u0446\u0438\u044f',
        ),
    ]
