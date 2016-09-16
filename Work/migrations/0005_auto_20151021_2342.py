# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0004_auto_20151020_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kva',
            field=models.IntegerField(default=None, verbose_name=b'\xe5\x8f\x97\xe7\x94\xb5\xe5\xae\xb9\xe9\x87\x8f(kva)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='line_type',
            field=models.CharField(default=None, max_length=255, verbose_name=b'\xe6\x8e\xa5\xe7\xba\xbf\xe6\x96\xb9\xe5\xbc\x8f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='manufacturer',
            field=models.CharField(default=None, max_length=255, verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe5\x8e\x82\xe5\xae\xb6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='meter_type',
            field=models.CharField(default=None, max_length=30, verbose_name=b'\xe8\xa1\xa8\xe8\xae\xa1\xe8\xa7\x84\xe7\xba\xa6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='metering_method',
            field=models.CharField(default=None, max_length=50, verbose_name=b'\xe8\xae\xa1\xe9\x87\x8f\xe6\x96\xb9\xe5\xbc\x8f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='tel_addr',
            field=models.CharField(default=None, max_length=20, verbose_name=b'\xe9\x80\x9a\xe4\xbf\xa1\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=False,
        ),
    ]
