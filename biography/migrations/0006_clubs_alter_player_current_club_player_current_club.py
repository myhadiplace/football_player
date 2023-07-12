# Generated by Django 4.2.1 on 2023-05-20 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0005_alter_player_born'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('club_country', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='Current_club',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='player',
            name='current_club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biography.clubs'),
        ),
    ]
