# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 13:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('jira_issue_id', models.IntegerField(null=True)),
                ('jira_issue_status', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='Installer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='installer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Installer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.Resource'),
        ),
        migrations.AddField(
            model_name='booking',
            name='scenario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Scenario'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
