# Generated by Django 2.0 on 2018-10-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0018_rota'),
    ]

    operations = [
        migrations.AddField(
            model_name='rota',
            name='Nome',
            field=models.CharField(default='Área x', max_length=25, unique=True),
        ),
    ]
