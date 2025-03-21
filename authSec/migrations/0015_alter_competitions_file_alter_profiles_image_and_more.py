# Generated by Django 5.0.4 on 2024-05-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authSec', '0014_alter_comments_downvote_alter_comments_upvote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitions',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='registeredcompetitions',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='authSec.competitions'),
        ),
    ]
