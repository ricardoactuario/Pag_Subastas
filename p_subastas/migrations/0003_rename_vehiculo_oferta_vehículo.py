# Generated by Django 5.1.3 on 2024-11-19 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_subastas', '0002_alter_oferta_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oferta',
            old_name='vehiculo',
            new_name='vehículo',
        ),
    ]
