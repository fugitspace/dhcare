# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-13 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_personcontact_mailing_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'get_latest_by': 'date_created'},
        ),
    ]
