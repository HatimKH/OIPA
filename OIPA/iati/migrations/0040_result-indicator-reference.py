# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati_vocabulary', '0005_result-indicator-reference'),
        ('iati', '0039_document-date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultIndicatorReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('indicator_uri', models.URLField(blank=True, null=True)),
                ('vocabulary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_vocabulary.IndicatorVocabulary')),
            ],
        ),
    ]
