# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcsproject', '0009_auto_20161006_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='emails',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='thesis',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
