# Generated by Django 3.2.6 on 2021-08-14 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210813_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 14, 12, 47, 40, 892941)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 14, 12, 47, 40, 891370)),
        ),
    ]
