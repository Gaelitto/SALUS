# Generated by Django 2.0 on 2018-11-06 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0027_auto_20181106_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rota',
            old_name='bairro',
            new_name='trajeto',
        ),
        migrations.RemoveField(
            model_name='rota',
            name='ruas',
        ),
    ]
