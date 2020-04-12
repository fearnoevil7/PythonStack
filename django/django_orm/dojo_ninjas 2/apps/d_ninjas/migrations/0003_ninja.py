# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-08 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_ninjas', '0002_auto_20191108_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ninja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('dojos', models.ManyToManyField(related_name='ninjas', to='d_ninjas.Dojo')),
            ],
        ),
    ]
