# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanitarianScopeVocabulary',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='budgetidentifiervocabulary',
            name='codelist_iati_version',
        ),
        migrations.RemoveField(
            model_name='budgetidentifiervocabulary',
            name='codelist_successor',
        ),
        migrations.RemoveField(
            model_name='geographicvocabulary',
            name='codelist_iati_version',
        ),
        migrations.RemoveField(
            model_name='geographicvocabulary',
            name='codelist_successor',
        ),
        migrations.RemoveField(
            model_name='policymarkervocabulary',
            name='codelist_iati_version',
        ),
        migrations.RemoveField(
            model_name='policymarkervocabulary',
            name='codelist_successor',
        ),
        migrations.RemoveField(
            model_name='regionvocabulary',
            name='codelist_iati_version',
        ),
        migrations.RemoveField(
            model_name='regionvocabulary',
            name='codelist_successor',
        ),
        migrations.RemoveField(
            model_name='sectorvocabulary',
            name='codelist_iati_version',
        ),
        migrations.RemoveField(
            model_name='sectorvocabulary',
            name='codelist_successor',
        ),
    ]
