# Generated by Django 4.2.1 on 2023-05-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0007_remove_player_current_club_alter_player_current_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='image',
        ),
        migrations.AddField(
            model_name='player',
            name='palyer_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]