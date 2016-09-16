# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0020_auto_20151119_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': '\u8282\u70b9\u4fe1\u606f', 'verbose_name_plural': '\u8282\u70b9\u4fe1\u606f'},
        ),
        migrations.AddField(
            model_name='user',
            name='remark1',
            field=models.CharField(max_length=255, null=True, verbose_name=b'remark'),
        ),
    ]
