# Generated by Django 5.0.4 on 2024-05-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0019_remove_profiles_user_user_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]
