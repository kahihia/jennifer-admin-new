# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20161022_0143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ['position']},
        ),
    ]