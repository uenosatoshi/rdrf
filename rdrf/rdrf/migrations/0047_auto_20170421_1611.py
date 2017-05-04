# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-21 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0046_auto_20170413_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ar', 'Arabic'), ('de', 'German')], max_length=2),
        ),
    ]
