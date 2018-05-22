# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main_image',
            field=models.BooleanField(default=False),
        ),
    ]
