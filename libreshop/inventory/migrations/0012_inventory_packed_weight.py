# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 18:29
from __future__ import unicode_literals

from django.db import migrations
import django_measurement.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20161019_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='packed_weight',
            field=django_measurement.models.MeasurementField(default=0.0, measurement_class='Mass'),
            preserve_default=False,
        ),
    ]