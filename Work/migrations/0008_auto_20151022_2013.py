# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0007_auto_20151022_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='addr_lat',
            field=models.DecimalField(default=None, null=True, verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='addr_lng',
            field=models.DecimalField(default=None, null=True, verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='line_type',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name=b'\xe6\x8e\xa5\xe7\xba\xbf\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
    ]
