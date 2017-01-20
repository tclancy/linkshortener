# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(db_index=True, max_length=255)),
                ('mobile_url', models.URLField(blank=True, max_length=255)),
                ('tablet_url', models.URLField(blank=True, max_length=255)),
                ('shortened', models.CharField(blank=True, db_index=True, max_length=20, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('hits', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]