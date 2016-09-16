# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0017_auto_20151108_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u8282\u70b9\u540d\u79f0')),
                ('district_name', models.CharField(max_length=255, verbose_name='\u6240\u5728\u53f0\u533a\u540d\u79f0')),
            ],
            options={
                'db_table': 'node',
                'verbose_name': '\u8def\u7ebf\u8282\u70b9',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7535\u7f51\u7528\u6237', 'verbose_name_plural': '\u7535\u7f51\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='xlsaddr',
            options={'verbose_name': '\u7528\u6237\u7ecf\u7eac\u5ea6\u4fe1\u606fxls\u6587\u4ef6', 'verbose_name_plural': '\u7528\u6237\u7ecf\u7eac\u5ea6\u4fe1\u606fxls\u6587\u4ef6'},
        ),
        migrations.AlterModelOptions(
            name='xlsuser',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606fxls\u6587\u4ef6', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606fxls\u6587\u4ef6'},
        ),
    ]
