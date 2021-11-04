# Generated by Django 3.0.11 on 2020-11-28 16:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='home_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(default=datetime.datetime(2020, 11, 28, 16, 39, 8, 141813, tzinfo=utc))),
                ('GrapefruitSoap', models.IntegerField(default=0)),
                ('LemongrassSugarScrub', models.IntegerField(default=0)),
                ('CharcoalClayFacialScrub', models.IntegerField(default=0)),
                ('LavenderSoap', models.IntegerField(default=0)),
                ('AloeVeraGoatMilkSoap', models.IntegerField(default=0)),
                ('PeppermintSoap', models.IntegerField(default=0)),
                ('EucalyptusSoap', models.IntegerField(default=0)),
                ('RawSoap', models.IntegerField(default=0)),
                ('CalendulaBurdockSalve', models.IntegerField(default=0)),
                ('SootheMeSalve', models.IntegerField(default=0)),
                ('LavenderLoofahSoap', models.IntegerField(default=0)),
                ('LemonPoppySeedSoap', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.ImageField(default='defaultProd.jpg', upload_to='product_pics')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Product')),
            ],
        ),
    ]