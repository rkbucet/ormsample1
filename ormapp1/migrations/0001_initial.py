# Generated by Django 4.2.2 on 2023-06-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(max_length=50)),
                ('Player_name', models.CharField(max_length=25)),
                ('Game_type', models.CharField(max_length=50)),
                ('Player_age', models.IntegerField()),
                ('Player_city', models.CharField(max_length=50)),
            ],
        ),
    ]
