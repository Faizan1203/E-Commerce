# Generated by Django 3.2.6 on 2021-08-13 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210813_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 13, 10, 54, 13, 663645)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 13, 10, 54, 13, 661987)),
        ),
    ]
