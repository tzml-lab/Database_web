# Generated by Django 2.2.3 on 2019-12-19 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20191219_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 12, 19, 18, 28, 41, 610526)),
        ),
    ]
