# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0025_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AddField(
            model_name='user',
            name='ima',
            field=models.CharField(max_length=255, null=True, verbose_name=b'image'),
        ),
    ]
