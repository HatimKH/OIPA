# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 01:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati_synchroniser', '0015_auto_20161025_1637'),
        ('permissions', '004_turn_on_publisher_constraints')
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='org_abbreviate',
            new_name='name',
        ),
    ]
