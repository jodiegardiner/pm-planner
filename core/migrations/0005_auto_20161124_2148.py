# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161124_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='height',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='weight',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
