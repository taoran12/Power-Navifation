# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0021_auto_20151212_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': '\u8def\u7ebf', 'verbose_name_plural': '\u8def\u7ebf\u4fe1\u606ffsaf'},
        ),
        migrations.AddField(
            model_name='user',
            name='ima',
            field=models.CharField(max_length=255, null=True, verbose_name=b'image'),
        ),
    ]
