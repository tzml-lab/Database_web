# Generated by Django 2.2.3 on 2019-12-19 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20191219_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
