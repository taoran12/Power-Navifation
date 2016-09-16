# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0014_auto_20151108_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xls_user', models.FileField(upload_to=b'./upload/lng_lat/')),
                ('xls_lng_lat', models.FileField(upload_to=b'.upload/user/')),
            ],
            options={
                'db_table': 'xls_file',
                'verbose_name': '\u4e0a\u4f20xls\u6587\u4ef6',
                'verbose_name_plural': '\u91c7\u96c6\u70b9\u4fe1\u606f',
            },
        ),
    ]
