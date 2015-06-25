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
                ('acc_no', models.IntegerField(serialize=False, primary_key=True)),
                ('acc_type', models.CharField(max_length=10)),
                ('total_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=10)),
                ('second_name', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=10)),
                ('password', models.IntegerField()),
                ('place', models.CharField(max_length=200)),
                ('contact_no', models.IntegerField()),
                ('joining_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('trans_id', models.IntegerField(serialize=False, primary_key=True)),
                ('last_available_balance', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('acc_no', models.ForeignKey(to='myprojects.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='cust_id',
            field=models.ForeignKey(to='myprojects.Customer'),
        ),
    ]
