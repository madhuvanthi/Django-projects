# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0004_auto_20150623_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='initial_deposit',
            field=models.IntegerField(default=0),
        ),
    ]
