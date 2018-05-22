# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_product_users_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to=shop.models.get_image_filename, verbose_name='image')),
                ('product', models.ForeignKey(on_delete='CASCADE', related_name='product', to='shop.Product', default=None)),
            ],
        ),
    ]
