# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='billing_lastname',
            new_name='billing_last_name',
        ),
    ]
