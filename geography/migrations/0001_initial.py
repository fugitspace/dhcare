# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Country Name')),
                ('alpha_two', models.CharField(blank=True, max_length=2, verbose_name='2-Letter Code')),
                ('alpha_three', models.CharField(blank=True, max_length=3, verbose_name='3-Letter Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='District Name')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='Abbreviation')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Region Name')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='Abbreviation')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='District Name')),
                ('code', models.CharField(blank=True, max_length=200, verbose_name='Abbreviation')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.District')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.Region'),
        ),
    ]
