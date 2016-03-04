# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-04 02:45
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fulfillment', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=32, null=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('sku', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(blank=True, max_length=2048, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/product')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64)),
                ('sub_sku', models.CharField(max_length=8, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('enabled', models.BooleanField(default=True)),
                ('drop_shipment_settings', models.ManyToManyField(blank=True, through='fulfillment.FulfillmentSettingValue', to='fulfillment.FulfillmentSetting')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variant'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='variant',
            unique_together=set([('product', 'name'), ('product', 'sub_sku')]),
        ),
        migrations.AlterUniqueTogether(
            name='component',
            unique_together=set([('variant', 'inventory')]),
        ),
    ]
