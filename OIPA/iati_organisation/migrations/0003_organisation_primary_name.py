# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_organisation', '0002_auto_20160421_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='primary_name',
            field=models.CharField(db_index=True, default='untitled, reparse to fix', max_length=150),
            preserve_default=False,
        ),
    ]
