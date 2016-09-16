# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0003_user_collection_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='collector',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe9\x87\x87\xe9\x9b\x86\xe8\x80\x85\xe5\x90\x8d\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='user',
            name='addr_lat',
            field=models.DecimalField(null=True, verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='addr_lng',
            field=models.DecimalField(null=True, verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
    ]
