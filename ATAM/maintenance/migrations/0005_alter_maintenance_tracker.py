# Generated by Django 4.0.1 on 2022-05-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_alter_maintenance_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='tracker',
            field=models.IntegerField(),
        ),
    ]
