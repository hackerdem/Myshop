# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20180519_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(related_name='products', default='1', to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(related_name='products', default='1', to='shop.Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='room',
            field=models.ForeignKey(related_name='products', default='1', to='shop.Room'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(related_name='products', default='1', to='shop.Size'),
        ),
    ]
