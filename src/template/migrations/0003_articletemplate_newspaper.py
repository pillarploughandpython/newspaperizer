# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0007_auto_20160912_1900'),
        ('template', '0002_auto_20160912_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletemplate',
            name='newspaper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='newspaper.Newspaper', verbose_name='newspaper'),
            preserve_default=False,
        ),
    ]