# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encounter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientvitals',
            name='patient',
        ),
        migrations.AddField(
            model_name='patientvitals',
            name='encounter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='encounter.Encounter'),
            preserve_default=False,
        ),
    ]
