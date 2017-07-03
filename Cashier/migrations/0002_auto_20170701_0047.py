# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-01 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='mods',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cashier.ProductMod'),
            preserve_default=False,
        ),
    ]