# Generated by Django 2.0 on 2018-10-27 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salus', '0009_auto_20181027_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extra',
            name='user',
        ),
        migrations.AlterField(
            model_name='visita',
            name='agente_da_visita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Extra',
        ),
    ]
