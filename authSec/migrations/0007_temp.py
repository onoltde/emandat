# Generated by Django 5.0.4 on 2024-05-03 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0006_delete_competitions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120, unique=True)),
            ],
        ),
    ]
