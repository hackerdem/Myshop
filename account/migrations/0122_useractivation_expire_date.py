# Generated by Django 2.0.5 on 2018-06-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0121_remove_useractivation_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivation',
            name='expire_date',
            field=models.CharField(default='12/12/2018', max_length=20),
        ),
    ]
