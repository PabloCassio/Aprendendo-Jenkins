# Generated by Django 2.1.7 on 2023-01-19 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230119_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 1, 19, 11, 47, 42, 436555)),
        ),
    ]
