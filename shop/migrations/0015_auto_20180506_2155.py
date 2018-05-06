# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20180506_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.RemoveField(
            model_name='size',
            name='id',
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, db_index=True),
        ),
    ]
