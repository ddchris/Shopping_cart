# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='uemail',
            field=models.EmailField(blank=True, default='@gmail.com', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='ugender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=2),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='uname',
            field=models.CharField(default='hello', max_length=30, unique=True),
        ),
    ]
