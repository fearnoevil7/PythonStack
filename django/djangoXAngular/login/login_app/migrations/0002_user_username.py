# Generated by Django 2.1.4 on 2020-04-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
