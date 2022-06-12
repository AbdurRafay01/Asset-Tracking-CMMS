# Generated by Django 4.0.1 on 2022-05-25 04:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker', models.IntegerField()),
                ('total_distance', models.DecimalField(decimal_places=4, max_digits=8, verbose_name='Total Distance Covered')),
                ('description', models.CharField(default='NO MAINTENANCE SCHEDULE', max_length=100)),
                ('maintenance_status', models.CharField(default='Not Pending', max_length=15)),
                ('maintenance_limit', models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(20)])),
            ],
        ),
    ]
