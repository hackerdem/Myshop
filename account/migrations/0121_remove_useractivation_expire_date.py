# Generated by Django 2.0.5 on 2018-05-25 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0120_auto_20180526_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivation',
            name='expire_date',
        ),
    ]
