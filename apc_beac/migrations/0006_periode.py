# Generated by Django 3.2.5 on 2021-07-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apc_beac', '0005_rename_num_tiers_mouvement_tiers'),
    ]

    operations = [
        migrations.CreateModel(
            name='periode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(max_length=254, null=True)),
                ('jour', models.CharField(max_length=254, null=True)),
            ],
        ),
    ]
