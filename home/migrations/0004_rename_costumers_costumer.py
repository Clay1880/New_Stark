# Generated by Django 4.0.1 on 2022-01-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_costumers_delete_information'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumers',
            new_name='Costumer',
        ),
    ]
