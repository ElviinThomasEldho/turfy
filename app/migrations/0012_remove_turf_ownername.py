# Generated by Django 4.2.7 on 2023-12-18 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_turf_ownername'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turf',
            name='ownerName',
        ),
    ]
