# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_synchroniser', '0006_auto_20160603_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='iatixmlsource',
            name='note_count',
            field=models.IntegerField(default=0),
        ),
    ]