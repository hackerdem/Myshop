# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0064_auto_20180522_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(default='ErdemDefault', max_length=128, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.ForeignKey(related_name='username', to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.AlterField(
            model_name='useractivation',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 3, 23, 40, 813303)),
        ),
    ]
