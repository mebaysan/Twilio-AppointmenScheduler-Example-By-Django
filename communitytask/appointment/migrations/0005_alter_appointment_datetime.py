# Generated by Django 3.2.9 on 2021-11-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20211126_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='datetime',
            field=models.DateTimeField(auto_created=True),
        ),
    ]