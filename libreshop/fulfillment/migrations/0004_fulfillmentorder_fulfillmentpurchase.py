# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 05:00
from __future__ import unicode_literals

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20160327_0102'),
        ('fulfillment', '0003_auto_20160306_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='FulfillmentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('order_id', models.CharField(max_length=8, unique=True, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tax', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FulfillmentPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('subtotal', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('tax', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fulfillment.FulfillmentOrder')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Purchase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
