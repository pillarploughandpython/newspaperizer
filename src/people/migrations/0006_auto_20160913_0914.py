# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160913_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='EyeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='color')),
            ],
        ),
        migrations.CreateModel(
            name='HairColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='color')),
            ],
        ),
        migrations.CreateModel(
            name='Haircut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('size', models.IntegerField(verbose_name='size')),
            ],
        ),
        migrations.CreateModel(
            name='HairParting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parting', models.CharField(max_length=255, verbose_name='parting')),
            ],
        ),
        migrations.RemoveField(
            model_name='hair',
            name='hairdress',
        ),
        migrations.RemoveField(
            model_name='hair',
            name='length',
        ),
        migrations.AlterField(
            model_name='cloth',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
        migrations.AlterField(
            model_name='face',
            name='eye',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.EyeColor', verbose_name='eye'),
        ),
        migrations.AlterField(
            model_name='face',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
        migrations.AlterField(
            model_name='hair',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.HairColor', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='hair',
            name='curling',
            field=models.BooleanField(verbose_name='curling'),
        ),
        migrations.AlterField(
            model_name='hair',
            name='face',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Face'),
        ),
        migrations.AlterField(
            model_name='hair',
            name='parting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.HairParting', verbose_name='parting'),
        ),
        migrations.AddField(
            model_name='hair',
            name='haircut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Haircut', verbose_name='haircut'),
        ),
    ]
