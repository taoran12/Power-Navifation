# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0016_auto_20151108_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xlsaddr',
            name='xls_addr',
            field=models.FileField(upload_to=b'./upload/lng_lat/', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='xlsuser',
            name='xls_user',
            field=models.FileField(upload_to=b'./upload/user/', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d'),
        ),
    ]
