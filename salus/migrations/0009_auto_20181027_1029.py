# Generated by Django 2.0 on 2018-10-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0008_auto_20181027_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencia',
            name='bairro',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='cidade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='responsavel',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='rua',
            field=models.CharField(max_length=200),
        ),
    ]