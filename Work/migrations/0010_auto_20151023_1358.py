# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0009_auto_20151022_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='addr_lat',
        ),
        migrations.RemoveField(
            model_name='location',
            name='addr_lng',
        ),
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(null=True, verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.DecimalField(null=True, verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='route',
            name='end',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe7\xbb\x88\xe7\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='route',
            name='record_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe9\x87\x87\xe9\x9b\x86\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='route',
            name='start',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe8\xb5\xb7\xe7\x82\xb9'),
        ),
    ]
