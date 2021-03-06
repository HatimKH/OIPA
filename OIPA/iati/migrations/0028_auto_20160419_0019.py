# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 00:19
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0027_convert_xdr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionrecipientcountry',
            name='xdr_value',
        ),
        migrations.RemoveField(
            model_name='transactionrecipientregion',
            name='xdr_value',
        ),
        migrations.RemoveField(
            model_name='transactionsector',
            name='xdr_value',
        ),
        migrations.AddField(
            model_name='transaction',
            name='cad_value',
            field=models.DecimalField(decimal_places=7, default=Decimal('0'), max_digits=20),
        ),
        migrations.AddField(
            model_name='transaction',
            name='eur_value',
            field=models.DecimalField(decimal_places=7, default=Decimal('0'), max_digits=20),
        ),
        migrations.AddField(
            model_name='transaction',
            name='gbp_value',
            field=models.DecimalField(decimal_places=7, default=Decimal('0'), max_digits=20),
        ),
        migrations.AddField(
            model_name='transaction',
            name='jpy_value',
            field=models.DecimalField(decimal_places=7, default=Decimal('0'), max_digits=20),
        ),
        migrations.AddField(
            model_name='transaction',
            name='usd_value',
            field=models.DecimalField(decimal_places=7, default=Decimal('0'), max_digits=20),
        ),
    ]
