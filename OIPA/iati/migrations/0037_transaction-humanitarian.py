# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0036_auto_20160602_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='humanitarian',
            field=models.NullBooleanField(),
        ),
    ]
