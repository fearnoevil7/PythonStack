# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-13 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='description',
            field=models.TextField(default='A very good show'),
            preserve_default=False,
        ),
    ]
