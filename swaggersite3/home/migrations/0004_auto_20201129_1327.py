# Generated by Django 3.0.11 on 2020-11-29 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201128_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 13, 27, 58, 119416, tzinfo=utc)),
        ),
    ]
