# Generated by Django 3.2.12 on 2023-11-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_center', '0003_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Новый', 'Новый'), ('В работе', 'В работе'), ('Готов', 'Готов'), ('Выдан', 'Выдан')], default='Новый', max_length=10),
        ),
    ]