# Generated by Django 3.2.23 on 2023-11-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=55, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=55, unique=True, verbose_name='URL')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menuitem', to='tree_menu.menugroup')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_menu.menuitem')),
            ],
            options={
                'verbose_name_plural': 'Menu Items',
            },
        ),
    ]
