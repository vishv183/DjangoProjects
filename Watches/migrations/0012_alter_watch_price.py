# Generated by Django 4.2.13 on 2024-06-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watches', '0011_alter_watch_bandwidth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
