# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-20 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0028_auto_20180117_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Date of death'),
        ),
    ]