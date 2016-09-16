# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0006_auto_20151021_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='collection_unit',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe9\x87\x87\xe9\x9b\x86\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='district_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8f\xb0\xe5\x8c\xba\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='district_number',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8f\xb0\xe5\x8c\xba\xe7\xbc\x96\xe7\xa0\x81'),
        ),
        migrations.AlterField(
            model_name='user',
            name='kva',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\x8f\x97\xe7\x94\xb5\xe5\xae\xb9\xe9\x87\x8f(kva)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='logical_addr',
            field=models.CharField(max_length=22, null=True, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='user',
            name='manufacturer',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe5\x8e\x82\xe5\xae\xb6'),
        ),
        migrations.AlterField(
            model_name='user',
            name='meter_number',
            field=models.CharField(max_length=22, null=True, verbose_name=b'\xe8\xa1\xa8\xe8\xae\xa1\xe5\xb1\x80\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='meter_type',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe8\xa1\xa8\xe8\xae\xa1\xe8\xa7\x84\xe7\xba\xa6'),
        ),
        migrations.AlterField(
            model_name='user',
            name='metering_method',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe8\xae\xa1\xe9\x87\x8f\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='user',
            name='power_unit',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\x89\x80'),
        ),
        migrations.AlterField(
            model_name='user',
            name='record_date',
            field=models.DateField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9c\x80\xe5\x90\x8e\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel_addr',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe9\x80\x9a\xe4\xbf\xa1\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='user',
            name='terminal_number',
            field=models.CharField(max_length=22, null=True, verbose_name=b'\xe7\xbb\x88\xe7\xab\xaf\xe5\xb1\x80\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unit',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_addr',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x88\xb7\xe5\x90\x8d'),
        ),
    ]
