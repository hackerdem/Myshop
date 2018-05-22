# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0066_auto_20180522_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(blank=True, max_length=64, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(default='3123', max_length=5, verbose_name='zip code'),
        ),
        migrations.AlterField(
            model_name='useractivation',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 18, 51, 56, 625982)),
        ),
    ]
