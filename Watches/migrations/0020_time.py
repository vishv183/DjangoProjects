# Generated by Django 5.0.6 on 2024-06-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watches', '0019_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
