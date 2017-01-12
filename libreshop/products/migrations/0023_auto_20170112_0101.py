# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-12 01:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20170112_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='_cost_cache_expiration',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc), verbose_name=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
