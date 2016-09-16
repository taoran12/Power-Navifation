# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('_id', models.IntegerField(serialize=False, primary_key=True)),
                ('route_id', models.CharField(max_length=255, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbfID')),
                ('addr_long', models.DecimalField(verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', max_digits=10, decimal_places=6)),
                ('addr_lat', models.DecimalField(verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', max_digits=10, decimal_places=6)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('_id', models.IntegerField(serialize=False, primary_key=True)),
                ('route_id', models.CharField(unique=True, max_length=255, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbfID')),
                ('start', models.CharField(max_length=255, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe8\xb5\xb7\xe7\x82\xb9')),
                ('end', models.CharField(max_length=255, verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe7\xbb\x88\xe7\x82\xb9')),
                ('record_date', models.DateField(verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe9\x87\x87\xe9\x9b\x86\xe6\x97\xb6\xe9\x97\xb4')),
                ('collector', models.CharField(max_length=50, verbose_name=b'\xe9\x87\x87\xe9\x9b\x86\xe8\x80\x85\xe5\x90\x8d\xe5\xad\x97')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', models.IntegerField(serialize=False, primary_key=True)),
                ('unit', models.CharField(max_length=255, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d')),
                ('power_unit', models.CharField(max_length=255, verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\x89\x80')),
                ('district_number', models.CharField(max_length=255, verbose_name=b'\xe5\x8f\xb0\xe5\x8c\xba\xe7\xbc\x96\xe7\xa0\x81')),
                ('district_name', models.CharField(max_length=255, verbose_name=b'\xe5\x8f\xb0\xe5\x8c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('user_id', models.CharField(unique=True, max_length=10, verbose_name=b'\xe6\x88\xb7\xe5\x8f\xb7')),
                ('user_name', models.CharField(max_length=50, verbose_name=b'\xe6\x88\xb7\xe5\x90\x8d')),
                ('user_addr', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('addr_long', models.DecimalField(verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6', max_digits=10, decimal_places=6)),
                ('addr_lat', models.DecimalField(verbose_name=b'\xe7\xba\xac\xe5\xba\xa6', max_digits=10, decimal_places=6)),
                ('terminal_number', models.CharField(max_length=22, verbose_name=b'\xe7\xbb\x88\xe7\xab\xaf\xe5\xb1\x80\xe5\x8f\xb7')),
                ('meter_number', models.CharField(max_length=22, verbose_name=b'\xe8\xa1\xa8\xe8\xae\xa1\xe5\xb1\x80\xe5\x8f\xb7')),
                ('logical_addr', models.CharField(max_length=22, verbose_name=b'\xe9\x80\xbb\xe8\xbe\x91\xe5\x9c\xb0\xe5\x9d\x80')),
                ('record_date', models.DateField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9c\x80\xe5\x90\x8e\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
