# Generated by Django 2.0 on 2018-11-07 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0033_auto_20181106_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trajeto',
            old_name='nome',
            new_name='rota',
        ),
    ]