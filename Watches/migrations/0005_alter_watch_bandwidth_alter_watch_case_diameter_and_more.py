# Generated by Django 4.2.13 on 2024-06-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watches', '0004_alter_watch_bandwidth_alter_watch_case_diameter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='bandwidth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watch',
            name='case_diameter',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watch',
            name='case_thickness',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watch',
            name='power_reserve',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watch',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watch',
            name='water_resistance',
            field=models.CharField(max_length=100),
        ),
    ]
