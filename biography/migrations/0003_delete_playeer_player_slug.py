# Generated by Django 4.2.1 on 2023-05-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0002_playeer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Playeer',
        ),
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
