# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20161124_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 24, 21, 48, 10, 972000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 24, 21, 48, 10, 971000, tzinfo=utc)),
        ),
    ]
