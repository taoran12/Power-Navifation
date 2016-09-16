# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0015_xls'),
    ]

    operations = [
        migrations.CreateModel(
            name='XlsAddr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xls_addr', models.FileField(upload_to=b'./upload/lng_lat/')),
            ],
            options={
                'db_table': 'xls_addr',
                'verbose_name': '\u4e0a\u4f20\u7528\u6237\u7ecf\u7eac\u5ea6\u4fe1\u606fxls\u6587\u4ef6',
                'verbose_name_plural': '\u4e0a\u4f20\u7528\u6237\u7ecf\u7eac\u5ea6\u4fe1\u606fxls\u6587\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='XlsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xls_user', models.FileField(upload_to=b'./upload/user/')),
            ],
            options={
                'db_table': 'xls_user',
                'verbose_name': '\u4e0a\u4f20\u7528\u6237\u4fe1\u606fxls\u6587\u4ef6',
                'verbose_name_plural': '\u4e0a\u4f20\u7528\u6237\u4fe1\u606fxls\u6587\u4ef6',
            },
        ),
        migrations.DeleteModel(
            name='Xls',
        ),
    ]
