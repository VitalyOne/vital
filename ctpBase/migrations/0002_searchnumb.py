# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctpBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchNumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.CharField(max_length=100)),
            ],
        ),
    ]
