# Generated by Django 4.0 on 2023-06-14 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_historialform_fecha_alter_historialform_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialform',
            name='hora',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 22, 8, 9, 556123)),
        ),
    ]