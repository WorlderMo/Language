# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-12 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
    ]
