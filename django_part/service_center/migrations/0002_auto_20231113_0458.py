# Generated by Django 3.2.12 on 2023-11-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_center', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts_roles',
            old_name='account_id',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='accounts_roles',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='executor_id',
            new_name='executor',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='account_id',
            new_name='account',
        ),
        migrations.AlterField(
            model_name='orders',
            name='closed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='repair_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
