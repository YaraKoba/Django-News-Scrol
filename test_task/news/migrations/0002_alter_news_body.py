# Generated by Django 3.2.23 on 2023-11-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(max_length=5000),
        ),
    ]
