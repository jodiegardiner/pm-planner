# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161124_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='hospital_num',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
