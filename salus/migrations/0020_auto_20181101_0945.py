# Generated by Django 2.0 on 2018-11-01 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0019_rota_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cidade',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='residencia',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
