# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-12 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20160411_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereview',
            name='overall_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]