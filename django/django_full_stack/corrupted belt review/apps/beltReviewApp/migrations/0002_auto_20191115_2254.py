# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-15 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltReviewApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ManyToManyField(related_name='books', to='beltReviewApp.User'),
        ),
    ]
