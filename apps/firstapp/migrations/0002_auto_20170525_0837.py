# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(max_length=6),
        ),
    ]
