# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0012_auto_20151023_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='update_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x88\xb0\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='user',
            name='update_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x88\xb0\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='record_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbf\xa1\xe6\x81\xaf\xe5\x9c\xa8\xe6\x9c\xac\xe5\x9c\xb0\xe4\xbf\xae\xe6\x94\xb9\xe7\x9a\x84\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
