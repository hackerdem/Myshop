# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20180504_2026'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
