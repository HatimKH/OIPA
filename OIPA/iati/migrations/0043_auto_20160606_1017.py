# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0042_auto_20160606_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultindicatorperiodactualdimension',
            name='result_indicator_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati.ResultIndicatorPeriod'),
        ),
        migrations.AlterField(
            model_name='resultindicatorperiodactuallocation',
            name='result_indicator_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati.ResultIndicatorPeriod'),
        ),
        migrations.AlterField(
            model_name='resultindicatorperiodtargetdimension',
            name='result_indicator_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati.ResultIndicatorPeriod'),
        ),
        migrations.AlterField(
            model_name='resultindicatorperiodtargetlocation',
            name='result_indicator_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati.ResultIndicatorPeriod'),
        ),
    ]
