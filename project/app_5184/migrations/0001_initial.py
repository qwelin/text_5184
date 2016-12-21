# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zx_id', models.CharField(max_length=12)),
                ('zk_name', models.CharField(max_length=8)),
                ('dat', models.CharField(max_length=6)),
                ('scort', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=20)),
                ('subject_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zkid', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=8)),
            ],
        ),
    ]
