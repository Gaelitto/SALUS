# Generated by Django 2.0 on 2018-11-06 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0023_auto_20181106_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rota',
            old_name='Nome',
            new_name='nome',
        ),
    ]
