# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0006_auto_20161110_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGames',
            fields=[
                ('sciencebook_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='book.ScienceBook')),
            ],
            options={
                'verbose_name': 'Book',
                'ordering': ['title'],
                'verbose_name_plural': 'Books',
            },
            bases=('book.sciencebook',),
        ),
    ]