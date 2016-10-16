# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcsproject', '0003_auto_20161002_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='authors',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='category',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='dept',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]