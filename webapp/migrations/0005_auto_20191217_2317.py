# Generated by Django 2.2.3 on 2019-12-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191217_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneyorlife',
            name='Dest_uID',
        ),
        migrations.RemoveField(
            model_name='moneyorlife',
            name='Src_uID',
        ),
        migrations.AddField(
            model_name='money',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='personporj',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]