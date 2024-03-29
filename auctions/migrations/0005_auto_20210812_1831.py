# Generated by Django 3.2.6 on 2021-08-12 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210812_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 18, 31, 38, 336152)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 18, 31, 38, 334715)),
        ),
    ]
