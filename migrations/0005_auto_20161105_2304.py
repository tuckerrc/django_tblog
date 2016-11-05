# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tblog', '0004_auto_20161102_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='Setting People Free', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(default='This will be replaced by the first 250 characters of the body text', max_length=250),
        ),
    ]