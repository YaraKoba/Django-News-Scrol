# Generated by Django 3.2.23 on 2023-11-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20231105_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
