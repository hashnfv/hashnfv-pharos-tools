# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='registration_complete',
            field=models.BooleanField(default=False),
        ),
    ]