# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0005_customer_initial_deposit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='initial_deposit',
        ),
    ]
