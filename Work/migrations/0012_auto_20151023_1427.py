# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0011_auto_20151023_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
