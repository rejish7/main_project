# Generated by Django 5.0.7 on 2024-08-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0004_appointment_slug_calltoaction_slug_department_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
