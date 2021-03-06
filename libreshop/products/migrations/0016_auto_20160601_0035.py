# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-01 00:35
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20160601_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='image',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Primary Point of Interest'),
        ),
    ]
