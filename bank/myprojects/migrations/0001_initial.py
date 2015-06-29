# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acc_no', models.AutoField(serialize=False, primary_key=True)),
                ('cust_id', models.IntegerField(blank=True)),
                ('acc_type', models.CharField(max_length=10)),
                ('total_balance', models.IntegerField()),
                ('transaction_type', models.IntegerField(blank=True)),
                ('transaction_amount', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('second_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=200)),
                ('contact_no', models.IntegerField()),
                ('acc_no', models.IntegerField(blank=True)),
                ('acc_type', models.CharField(max_length=50)),
            ],
        ),
    ]
