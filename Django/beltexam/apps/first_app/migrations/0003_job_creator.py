# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-21 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_category_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='myjobs', to='first_app.User'),
            preserve_default=False,
        ),
    ]