# Generated by Django 3.2.5 on 2021-07-31 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apc_beac', '0009_tiers_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouvement',
            name='numero',
        ),
    ]
