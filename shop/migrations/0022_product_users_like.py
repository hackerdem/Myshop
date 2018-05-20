# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0021_auto_20180520_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users_like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='products_liked', blank=True),
        ),
    ]
