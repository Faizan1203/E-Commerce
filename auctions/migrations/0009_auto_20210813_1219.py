# Generated by Django 3.2.6 on 2021-08-13 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210813_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 13, 12, 19, 34, 396779)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 13, 12, 19, 34, 394675)),
        ),
    ]
