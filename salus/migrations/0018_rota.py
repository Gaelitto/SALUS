# Generated by Django 2.0 on 2018-10-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0017_auto_20181027_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trajeto', models.ManyToManyField(to='salus.Bairro')),
            ],
        ),
    ]
