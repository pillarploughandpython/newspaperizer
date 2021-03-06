# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20160922_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='bookgenre',
            options={'ordering': ['title'], 'verbose_name': 'Book genre', 'verbose_name_plural': 'Book genres'},
        ),
        migrations.RemoveField(
            model_name='bookgenre',
            name='parent',
        ),
        migrations.AddField(
            model_name='bookgenre',
            name='children',
            field=models.ManyToManyField(blank=True, to='book.BookGenre', verbose_name='Parent genre'),
        ),
    ]
