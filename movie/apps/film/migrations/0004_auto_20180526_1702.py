# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-26 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20180526_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='logo',
            field=models.ImageField(default=b'image/default.png', upload_to=b'banner/%Y/%m', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2'),
        ),
        migrations.AlterField(
            model_name='preview',
            name='logo',
            field=models.ImageField(default=b'image/default.png', upload_to=b'banner/%Y/%m', verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2'),
        ),
    ]
