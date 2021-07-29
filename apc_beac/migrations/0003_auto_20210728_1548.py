# Generated by Django 3.2.5 on 2021-07-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apc_beac', '0002_alter_mouvement_num_tiers2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mouvement',
            old_name='num_tiers1',
            new_name='centre',
        ),
        migrations.RenameField(
            model_name='mouvement',
            old_name='num_tiers2',
            new_name='tiers',
        ),
        migrations.AddField(
            model_name='mouvement',
            name='compte',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='solde',
            field=models.CharField(max_length=254, null=True),
        ),
    ]