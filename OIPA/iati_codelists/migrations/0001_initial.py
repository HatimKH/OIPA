# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iati_vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDateType',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityScope',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityStatus',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='AidType',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='AidTypeCategory',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='AidTypeFlag',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetIdentifier',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetIdentifierSector',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetIdentifierSectorCategory',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetStatus',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='CollaborationType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ConditionType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='CRSChannelCode',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='DescriptionType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='DisbursementChannel',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.TextField(default=b'')),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
            options={
                'verbose_name': 'Document category',
                'verbose_name_plural': 'Document categories',
            },
        ),
        migrations.CreateModel(
            name='DocumentCategoryCategory',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='FileFormat',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
                ('category', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=220)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceTypeCategory',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='FlowType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='GazetteerAgency',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='GeographicalPrecision',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='GeographicExactness',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='GeographicLocationClass',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='GeographicLocationReach',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='HumanitarianScopeType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='IndicatorMeasure',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LoanRepaymentPeriod',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LoanRepaymentType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LocationTypeCategory',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationIdentifier',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(default=None, max_length=30, null=True)),
                ('name', models.CharField(default=None, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationRegistrationAgency',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField(default=b'')),
                ('category', models.CharField(max_length=2)),
                ('url', models.URLField(default=b'')),
                ('public_database', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationRole',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='OtherFlags',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='OtherIdentifierType',
            fields=[
                ('code', models.CharField(default=b'', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyMarker',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'')),
                ('vocabulary', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_vocabulary.PolicyMarkerVocabulary')),
            ],
        ),
        migrations.CreateModel(
            name='PolicySignificance',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='PublisherType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedActivityType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ResultType',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
                ('percentage', models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectorCategory',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='TiedStatus',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ValueType',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='VerificationStatus',
            fields=[
                ('code', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('code', models.CharField(default=b'', max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('description', models.TextField(default=b'')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='sector',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.SectorCategory'),
        ),
        migrations.AddField(
            model_name='sector',
            name='vocabulary',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_vocabulary.SectorVocabulary'),
        ),
        migrations.AddField(
            model_name='locationtype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.LocationTypeCategory'),
        ),
        migrations.AddField(
            model_name='financetype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.FinanceTypeCategory'),
        ),
        migrations.AddField(
            model_name='documentcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.DocumentCategoryCategory'),
        ),
        migrations.AddField(
            model_name='budgetidentifiersector',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.BudgetIdentifierSectorCategory'),
        ),
        migrations.AddField(
            model_name='budgetidentifier',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.BudgetIdentifierSector'),
        ),
        migrations.AddField(
            model_name='budgetidentifier',
            name='vocabulary',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_vocabulary.BudgetIdentifierVocabulary'),
        ),
        migrations.AddField(
            model_name='aidtype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.AidTypeCategory'),
        ),
    ]
