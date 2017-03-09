# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 14:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]