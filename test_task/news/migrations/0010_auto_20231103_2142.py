# Generated by Django 3.2.23 on 2023-11-03 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20231103_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 18, 42, 50, 758617)),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/media'),
        ),
    ]
