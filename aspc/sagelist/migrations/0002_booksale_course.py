# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-28 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20160417_1327'),
        ('sagelist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksale',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
