# Generated by Django 5.0.4 on 2024-05-03 03:15

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0007_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('startdate', models.DateField(default=django.utils.timezone.now)),
                ('enddate', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=1200)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ManyToManyField(to='authSec.types')),
            ],
        ),
    ]
