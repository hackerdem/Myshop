# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180428_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('shipping_first_name', models.CharField(max_length=50)),
                ('shipping_last_name', models.CharField(max_length=50)),
                ('shipping_email', models.EmailField(max_length=254)),
                ('shipping_address', models.CharField(max_length=250)),
                ('shipping_landmark', models.CharField(max_length=250)),
                ('shipping_country', models.CharField(max_length=50)),
                ('shipping_state', models.CharField(max_length=50)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_postcode', models.CharField(max_length=50)),
                ('billing_first_name', models.CharField(max_length=50)),
                ('billing_lastname', models.CharField(max_length=50)),
                ('billing_email', models.EmailField(max_length=254)),
                ('billing_address', models.CharField(max_length=250)),
                ('billing_landmark', models.CharField(max_length=250)),
                ('billing_country', models.CharField(max_length=50)),
                ('billing_state', models.CharField(max_length=50)),
                ('billing_city', models.CharField(max_length=50)),
                ('billing_postcode', models.CharField(max_length=50)),
                ('use_shipping_for_billing', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(to='shop.Product', related_name='purchase_items')),
                ('purchase', models.ForeignKey(to='purchases.Purchase', related_name='items')),
            ],
        ),
    ]
