# Generated by Django 3.2.5 on 2021-07-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apc_beac', '0006_periode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiers',
            old_name='description',
            new_name='description1',
        ),
        migrations.AddField(
            model_name='tiers',
            name='description2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tiers',
            name='description3',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tiers',
            name='description4',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tiers',
            name='description5',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tiers',
            name='description6',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tiers',
            name='description7',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
