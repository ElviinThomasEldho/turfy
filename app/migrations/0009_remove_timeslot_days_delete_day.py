# Generated by Django 4.2.7 on 2023-12-18 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_payment_datecreated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='days',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
