# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0003_auto_20150623_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acc_no',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
