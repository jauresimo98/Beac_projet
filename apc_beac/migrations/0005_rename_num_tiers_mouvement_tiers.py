# Generated by Django 3.2.5 on 2021-07-28 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apc_beac', '0004_auto_20210728_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mouvement',
            old_name='num_tiers',
            new_name='tiers',
        ),
    ]
