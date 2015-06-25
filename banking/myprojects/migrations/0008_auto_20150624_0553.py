# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0007_auto_20150623_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trans_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
