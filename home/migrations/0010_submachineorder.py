# Generated by Django 4.0.1 on 2022-01-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_sniperorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMachineOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('gun_name', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=20)),
                ('mode_info', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
