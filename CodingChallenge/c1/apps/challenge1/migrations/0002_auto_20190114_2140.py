# Generated by Django 2.0.6 on 2019-01-14 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pwdhash',
            new_name='password',
        ),
    ]
