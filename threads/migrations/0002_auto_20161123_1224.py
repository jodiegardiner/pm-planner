# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 12:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 23, 12, 24, 35, 90000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 23, 12, 24, 35, 88000, tzinfo=utc)),
        ),
    ]