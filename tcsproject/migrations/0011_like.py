# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tcsproject', '0010_auto_20161010_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=500)),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcsproject.Thesis')),
            ],
        ),
    ]