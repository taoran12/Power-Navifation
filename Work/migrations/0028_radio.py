# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0027_auto_20160711_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=255, verbose_name='\u6237\u53f7')),
                ('md5', models.CharField(max_length=255, verbose_name='md5\u503c')),
            ],
            options={
                'db_table': 'radio',
                'verbose_name': '\u8bed\u97f3\u4fe1\u606f',
                'verbose_name_plural': '\u8bed\u97f3\u4fe1\u606f',
            },
        ),
    ]
