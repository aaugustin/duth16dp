# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 20:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgbench', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE pgbench_history'
            '    ADD COLUMN hid SERIAL PRIMARY KEY',
            'ALTER TABLE pgbench_history'
            '    DROP COLUMN hid',
        ),
    ]