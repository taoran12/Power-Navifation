# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0013_auto_20151027_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': '\u91c7\u96c6\u70b9', 'verbose_name_plural': '\u91c7\u96c6\u70b9\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': '\u8def\u7ebf', 'verbose_name_plural': '\u8def\u7ebf\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AlterModelTable(
            name='location',
            table='location',
        ),
        migrations.AlterModelTable(
            name='route',
            table='route',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
