# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20160416_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='engagement_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursereview',
            name='engagement_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='engagement_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
