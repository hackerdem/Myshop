# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_auto_20180519_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='email address', unique=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='useractivation',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 19, 5, 41, 49, 969456)),
        ),
    ]
