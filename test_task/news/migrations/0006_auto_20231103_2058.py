# Generated by Django 3.2.23 on 2023-11-03 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20231103_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 17, 58, 50, 758114)),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]