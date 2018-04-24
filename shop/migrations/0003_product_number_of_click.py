# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180417_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_of_click',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
