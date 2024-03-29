# Generated by Django 2.2.3 on 2019-12-14 05:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uID', models.CharField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uID', models.CharField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('Name', models.CharField(max_length=50)),
                ('Time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.GroupInfo')),
                ('uID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='PersonPorj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('uID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='MoneyOrLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('moneyValue', models.IntegerField()),
                ('gpID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.GroupInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PorG', models.CharField(choices=[('P', 'p'), ('G', 'g')], max_length=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('InorOut', models.CharField(choices=[('I', 'I'), ('O', 'O')], max_length=1)),
                ('ItemType', models.CharField(max_length=10)),
                ('ItemName', models.CharField(max_length=10)),
                ('gpID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.GroupInfo')),
                ('pName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.PersonPorj')),
                ('uID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='GroupProj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpID', models.CharField(max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('Name', models.CharField(max_length=20)),
                ('CreatedBy', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
                ('gID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.GroupInfo')),
            ],
        ),
    ]
