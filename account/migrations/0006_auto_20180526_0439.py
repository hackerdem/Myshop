# Generated by Django 2.0.5 on 2018-05-25 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180526_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivation',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 26, 4, 39, 8, 526580)),
        ),
    ]