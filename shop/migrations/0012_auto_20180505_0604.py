# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20180505_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.ForeignKey(default=1, related_name='products', to='shop.Room'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default=1, related_name='products', to='shop.Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=1, related_name='products', to='shop.Size'),
        ),
    ]
