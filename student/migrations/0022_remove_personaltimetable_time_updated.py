# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-15 23:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_remove_personaltimetable__semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaltimetable',
            name='time_updated',
        ),
    ]