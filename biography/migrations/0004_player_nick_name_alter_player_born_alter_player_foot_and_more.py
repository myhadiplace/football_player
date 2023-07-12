# Generated by Django 4.2.1 on 2023-05-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0003_delete_playeer_player_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nick_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='born',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='foot',
            field=models.CharField(choices=[('right', 'Right'), ('left', 'Left')], max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]