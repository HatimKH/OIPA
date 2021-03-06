# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_vocabulary', '0004_auto_20160602_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorVocabulary',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
                ('url', models.URLField()),
            ],
        ),
    ]
