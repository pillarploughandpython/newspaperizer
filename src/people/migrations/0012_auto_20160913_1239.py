# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20160913_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastsize',
            name='size',
            field=models.CharField(max_length=255, verbose_name='size'),
        ),
    ]
