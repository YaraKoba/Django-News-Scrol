# Generated by Django 3.2.23 on 2023-11-04 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20231103_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='news',
            name='tag',
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='news', to='news.Tag'),
        ),
    ]
