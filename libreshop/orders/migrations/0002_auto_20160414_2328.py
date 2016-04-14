# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 23:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='origin_ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_card_expiration_date',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator('^(0[1-9]|1[0-2])[/-]\\d{2}$', code='Invalid expiration date', message='Expiration date must be in MM/YY or MM-YY format')], verbose_name='Expiration Date'),
        ),
    ]
