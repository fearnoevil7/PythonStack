# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-12 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Something about the author'),
            preserve_default=False,
        ),
    ]
