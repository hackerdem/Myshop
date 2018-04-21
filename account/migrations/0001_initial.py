# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=64, verbose_name='Email address')),
                ('name', models.TextField(max_length=64, verbose_name='name')),
                ('surname', models.TextField(max_length=128, verbose_name='Family name')),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('address_1', models.CharField(max_length=128, verbose_name='address', blank=True)),
                ('address_2', models.CharField(max_length=128, verbose_name="address cont'd", blank=True)),
                ('city', models.CharField(max_length=64, verbose_name='city', blank=True)),
                ('zip_code', models.CharField(max_length=4, default='3123', verbose_name='zip code')),
                ('phone', models.TextField()),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
