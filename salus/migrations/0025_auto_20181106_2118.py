# Generated by Django 2.0 on 2018-11-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0024_auto_20181106_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rota',
            name='trajeto',
            field=models.ManyToManyField(to='salus.Bairro'),
        ),
    ]
