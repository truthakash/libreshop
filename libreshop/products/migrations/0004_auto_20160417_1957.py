# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 19:57
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image_ppoi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Primary Point of Interest'),
        ),
    ]
