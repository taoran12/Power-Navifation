# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0005_auto_20151021_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='line_type',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x8e\xa5\xe7\xba\xbf\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
    ]
