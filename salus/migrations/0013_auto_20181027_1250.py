# Generated by Django 2.0 on 2018-10-27 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0012_auto_20181027_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='residencia',
            name='bairro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salus.Bairro'),
        ),
    ]