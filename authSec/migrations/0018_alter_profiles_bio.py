# Generated by Django 5.0.4 on 2024-05-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0017_alter_competitions_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
