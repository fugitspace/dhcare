# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 04:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patientcontact_patientdemographic_patientvitals_vitals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patientvitals',
            options={'verbose_name_plural': 'Patient Vitals'},
        ),
        migrations.AlterModelOptions(
            name='vitals',
            options={'verbose_name_plural': 'Vitals'},
        ),
    ]
