# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-18 02:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160307_0142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attribute_Value',
            new_name='AttributeValue',
        ),
    ]
