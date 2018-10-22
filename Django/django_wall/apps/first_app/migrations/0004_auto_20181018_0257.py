# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-18 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20181017_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='parent_message',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='first_app.User'),
        ),
    ]