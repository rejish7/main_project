# Generated by Django 5.0.7 on 2024-08-01 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name': 'Hospital', 'verbose_name_plural': 'Hospital'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Setting'},
        ),
    ]
