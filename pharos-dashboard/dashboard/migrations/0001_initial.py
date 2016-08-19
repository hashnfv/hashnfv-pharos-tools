# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slavename', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('bookable', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
    ]
