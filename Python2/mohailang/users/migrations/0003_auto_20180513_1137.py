# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_login_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default='1996-09-28', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='\u83ab\u6d77\u6d6a', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='13112355359', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default='\u7537', max_length=3),
        ),
    ]