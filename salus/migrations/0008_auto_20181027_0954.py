# Generated by Django 2.0 on 2018-10-27 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0007_justificar_visita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visita',
            old_name='residencia_visitada',
            new_name='residencia_da_visita',
        ),
    ]