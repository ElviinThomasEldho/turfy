# Generated by Django 4.2.7 on 2023-12-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_timeslot_choice_timeslot_endampm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(max_length=10, null=True, verbose_name='Total Amount '),
        ),
        migrations.AlterField(
            model_name='payment',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Payment Screenshot Upload'),
        ),
    ]
