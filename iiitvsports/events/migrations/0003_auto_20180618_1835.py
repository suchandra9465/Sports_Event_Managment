# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-18 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_football_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='football',
            old_name='user',
            new_name='created_by',
        ),
    ]
