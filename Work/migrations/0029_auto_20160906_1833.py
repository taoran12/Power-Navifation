# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0028_radio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='md5',
            field=models.CharField(unique=True, max_length=255, verbose_name='md5\u503c'),
        ),
    ]
