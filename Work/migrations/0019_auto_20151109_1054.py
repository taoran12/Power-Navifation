# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0018_auto_20151108_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='district_name',
            new_name='dis_num',
        ),
        migrations.AddField(
            model_name='node',
            name='record_date',
            field=models.DateTimeField(null=True, verbose_name='\u8282\u70b9\u91c7\u96c6\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='node',
            name='update_date',
            field=models.DateTimeField(null=True, verbose_name='\u7528\u6237\u4fe1\u606f\u4e0a\u4f20\u5230\u670d\u52a1\u5668\u7684\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='route',
            name='distance',
            field=models.FloatField(null=True, verbose_name=b'\xe8\xb7\x9d\xe7\xa6\xbb'),
        ),
    ]
