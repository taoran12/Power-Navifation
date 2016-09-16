# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0010_auto_20151023_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
