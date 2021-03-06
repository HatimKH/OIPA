
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 17:14
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.management import update_contenttypes

from iati.parser import post_save
from currency_convert import convert

def convert_xdr_values(apps, schema_editor):
    """
    convert all transaction's xdr values
    takes ~20 mins
    """
    update_contenttypes(apps.get_app_config('iati'), interactive=False) # make sure all content types exist
    
    try: # don't run on first migration
        Budget = apps.get_model('iati', 'Budget')
        Transaction = apps.get_model('iati', 'Transaction')
        Activity = apps.get_model('iati', 'Activity')

        TranasctionSector = apps.get_model('iati', 'TranasctionSector')
        TransactionRecipientCountry = apps.get_model('iati', 'TransactionRecipientCountry')
        TransactionRecipientSector = apps.get_model('iati', 'TransactionRecipientSector')

    except:
        return

    for budget in Budget.objects.all().iterator():
        budget.xdr_value = convert.to_xdr(budget.currency_id, budget.value_date, budget.value)
        budget.save()

    for transaction in Transaction.objects.all().iterator():
        transaction.xdr_value = convert.to_xdr(transaction.currency_id, transaction.value_date, transaction.value)
        transaction.save()

    for activity in Activity.objects.all().iterator():
        TransactionSector.objects.all().filter(transaction__activity=activity).delete()
        TransactionRecipientCountry.objects.all().filter(transaction__activity=activity).delete()
        TransactionRecipientSector.objects.all().filter(transaction__activity=activity).delete()

        post_save.set_sector_transaction(activity)
        post_save.set_country_region_transaction(activity)

class Migration(migrations.Migration):
    dependencies = [
        ('iati', '0026_auto_20160418_1506'),
    ]

    operations = [
        migrations.RunPython(convert_xdr_values),
    ]
