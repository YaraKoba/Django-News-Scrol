# Generated by Django 3.2.23 on 2023-11-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20231104_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]