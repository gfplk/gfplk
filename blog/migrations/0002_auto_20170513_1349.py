# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(choices=[('1', '男'), ('2', '女'), ('3', '保密')], max_length=1),
        ),
    ]
