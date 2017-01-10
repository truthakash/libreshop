# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-10 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_cost_of_goods_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cost_of_goods_sold',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True),
        ),
    ]
