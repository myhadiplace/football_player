# Generated by Django 4.2.1 on 2023-05-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('born', models.IntegerField()),
                ('birth_place', models.CharField(max_length=100)),
                ('foot', models.CharField(max_length=10)),
                ('Current_club', models.CharField(max_length=50)),
                ('image', models.URLField()),
            ],
        ),
    ]
