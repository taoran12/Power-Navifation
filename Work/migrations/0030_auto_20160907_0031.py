# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0029_auto_20160906_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='md5',
        ),
        migrations.AddField(
            model_name='image',
            name='content',
            field=models.ImageField(default=b'a', upload_to=b'images'),
        ),
    ]
