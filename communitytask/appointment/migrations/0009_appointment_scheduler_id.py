# Generated by Django 3.2.9 on 2021-11-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_rename_datetime_appointment_appointment_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='scheduler_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
