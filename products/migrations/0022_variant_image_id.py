# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_variant_mattress_pieces'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='image_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]