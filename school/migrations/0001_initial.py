# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('info', models.TextField()),
                ('summary', models.CharField(unique=True, max_length=64)),
                ('category', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='AppCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(unique=True, max_length=8)),
                ('name', models.CharField(unique=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='AppDeveloper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AppRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_requirement', models.CharField(unique=True, max_length=16)),
                ('released_at', models.DateTimeField()),
                ('release_info', models.TextField()),
                ('download_count', models.IntegerField()),
                ('app', models.ForeignKey(to='school.App')),
            ],
        ),
        migrations.CreateModel(
            name='AppTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=8)),
            ],
        ),
    ]
