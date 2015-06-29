# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionid', models.AutoField(serialize=False, primary_key=True, db_column=b'transactionId')),
                ('transactiontype', models.IntegerField(null=True, db_column=b'transactionType', blank=True)),
                ('transactionamount', models.IntegerField(null=True, db_column=b'transactionAmount', blank=True)),
            ],
            options={
                'db_table': 'transaction',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
    ]
