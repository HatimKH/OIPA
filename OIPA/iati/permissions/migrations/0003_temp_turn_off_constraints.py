# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-31 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0002_auto_20161031_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='OrganisationAdminGroup',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, db_constraint=False, to='iati_synchroniser.Publisher', unique=True)
        ),
        migrations.AlterField(
            model_name='OrganisationGroup',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, db_constraint=False, to='iati_synchroniser.Publisher', unique=True)
        )
    ]
