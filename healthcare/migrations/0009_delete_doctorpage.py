# Generated by Django 5.0.7 on 2024-08-10 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0008_delete_overviewsection_delete_overviewsetting'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DoctorPage',
        ),
    ]
