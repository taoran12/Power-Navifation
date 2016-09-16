# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='addr_long',
            new_name='addr_lng',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='addr_long',
            new_name='addr_lng',
        ),
    ]
