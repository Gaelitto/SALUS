# Generated by Django 2.0.4 on 2018-10-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0002_auto_20181019_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='residencia',
            name='bairro',
            field=models.TextField(default='a'),
        ),
    ]
