# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antispam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAcessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(db_index=True, unique=True)),
                ('last_accessed', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]