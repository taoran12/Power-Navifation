# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0008_auto_20151022_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='record_date',
            field=models.DateTimeField(verbose_name=b'\xe8\xb7\xaf\xe7\xba\xbf\xe9\x87\x87\xe9\x9b\x86\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='record_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9c\x80\xe5\x90\x8e\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
