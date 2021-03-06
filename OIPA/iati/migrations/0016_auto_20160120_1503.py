# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 15:03
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import Q
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0015_auto_20160107_1301'),
    ]

    def delete_invalid_transactions(apps, schema_editor):
        Transaction = apps.get_model('iati', 'Transaction')
        db_alias = schema_editor.connection.alias

        query = Q(value_date__isnull=True) | Q(transaction_date__isnull=True) | Q(transaction_type__isnull=True)

        Transaction.objects.all().filter(query).delete()


    operations = [
        migrations.RunPython(delete_invalid_transactions),
    ]
