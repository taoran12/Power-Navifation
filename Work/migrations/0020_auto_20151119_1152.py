# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0019_auto_20151109_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='lat',
            field=models.DecimalField(null=True, verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
        migrations.AddField(
            model_name='node',
            name='lng',
            field=models.DecimalField(null=True, verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
    ]
