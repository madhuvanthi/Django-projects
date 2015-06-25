# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0006_remove_customer_initial_deposit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cust_id',
            field=models.IntegerField(blank=True),
        ),
    ]
