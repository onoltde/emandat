# Generated by Django 5.0.4 on 2024-05-09 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0018_alter_profiles_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='authSec.profiles'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='registeredcompetitions',
            field=models.ManyToManyField(blank=True, related_name='profile', to='authSec.competitions'),
        ),
    ]
