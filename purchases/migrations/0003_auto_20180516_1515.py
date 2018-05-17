# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
        ('purchases', '0002_auto_20180503_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='coupon',
            field=models.ForeignKey(to='coupons.Coupon', blank=True, related_name='purchases', null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
