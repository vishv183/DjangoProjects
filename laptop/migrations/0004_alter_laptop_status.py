# Generated by Django 4.2.13 on 2024-06-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0003_rename_laptops_laptop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]
