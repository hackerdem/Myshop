# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20180428_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img_product_id',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
