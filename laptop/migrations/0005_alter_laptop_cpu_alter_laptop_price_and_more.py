# Generated by Django 4.2.13 on 2024-06-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0004_alter_laptop_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='cpu',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='screen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
