# Generated by Django 4.2.2 on 2024-01-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_historicalvegetable_historicalrecord_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
