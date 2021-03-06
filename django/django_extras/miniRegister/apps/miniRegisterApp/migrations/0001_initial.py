# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 16:18
from __future__ import unicode_literals

import apps.miniRegisterApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45, validators=[apps.miniRegisterApp.models.validateLengthGreaterThanTwo])),
                ('last_name', models.CharField(max_length=45, validators=[apps.miniRegisterApp.models.validateLengthGreaterThanTwo])),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=45, validators=[apps.miniRegisterApp.models.AtleastEight])),
                ('confirmation', models.CharField(max_length=45, validators=[apps.miniRegisterApp.models.AtleastEight])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
