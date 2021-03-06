# Generated by Django 3.2.5 on 2021-07-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mouvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode', models.CharField(max_length=254, null=True)),
                ('solde', models.IntegerField(blank=True, null=True)),
                ('num_tiers1', models.IntegerField(blank=True, null=True)),
                ('num_tiers2', models.IntegerField(blank=True, null=True)),
                ('num_tiers', models.CharField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_tiers', models.CharField(max_length=254, null=True)),
                ('destinataire', models.CharField(max_length=254, null=True)),
                ('description', models.CharField(max_length=254, null=True)),
            ],
        ),
    ]
