# Generated by Django 2.0.4 on 2018-11-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0020_auto_20181101_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sigla', models.CharField(max_length=2, unique=True)),
            ],
        ),
    ]
