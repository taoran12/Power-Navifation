# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0002_auto_20151020_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collection_unit',
            field=models.CharField(default=None, max_length=255, verbose_name=b'\xe9\x87\x87\xe9\x9b\x86\xe5\x8d\x95\xe4\xbd\x8d'),
            preserve_default=False,
        ),
    ]
