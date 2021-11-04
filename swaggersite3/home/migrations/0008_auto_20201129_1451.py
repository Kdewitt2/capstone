# Generated by Django 3.0.11 on 2020-11-29 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201129_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='homepost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 14, 51, 0, 793669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 14, 51, 0, 794079, tzinfo=utc)),
        ),
    ]