# Generated by Django 5.0.6 on 2024-06-22 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0026_especiedb_remove_resguardo_gatodb_gato_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Especiedb',
            new_name='Especiesdb',
        ),
        migrations.AlterModelOptions(
            name='animalesdb',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animales'},
        ),
        migrations.AlterModelOptions(
            name='especiesdb',
            options={'verbose_name': 'Especies'},
        ),
        migrations.AlterModelOptions(
            name='resguardodb',
            options={'verbose_name': 'Resguardo'},
        ),
        migrations.AlterModelTable(
            name='animalesdb',
            table='Animales',
        ),
        migrations.AlterModelTable(
            name='especiesdb',
            table='Especies',
        ),
        migrations.AlterModelTable(
            name='resguardodb',
            table='Resguardo',
        ),
    ]