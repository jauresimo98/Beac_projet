# Generated by Django 3.2.5 on 2021-07-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apc_beac', '0008_merge_0006_mouvement_numero_0007_auto_20210729_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiers',
            name='description',
            field=models.CharField(max_length=254, null=True),
        ),
    ]