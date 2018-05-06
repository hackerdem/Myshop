# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20180506_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default='ng', to='shop.Color', related_name='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='room',
            field=models.ForeignKey(default='ng', to='shop.Room', related_name='products'),
        ),
    ]
