# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0022_auto_20160707_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ima',
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2016, 7, 10, 12, 24, 36, 922757), upload_to=b'photos'),
            preserve_default=False,
        ),
    ]
