# Generated by Django 5.0.6 on 2024-06-21 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0020_alter_vacunas_perrodb_options_vacunas_gatodb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacunas_gatodb',
            options={'verbose_name': 'Vacunas Gato', 'verbose_name_plural': 'Vacunas_Gatos'},
        ),
        migrations.AlterModelOptions(
            name='vacunas_perrodb',
            options={'verbose_name': 'Vacunas_perro', 'verbose_name_plural': 'Vacunas_perros'},
        ),
        migrations.RemoveField(
            model_name='perrosdb',
            name='obs',
        ),
        migrations.AlterModelTable(
            name='perrosdb',
            table='Perro',
        ),
        migrations.AlterModelTable(
            name='vacunas_gatodb',
            table='Vacunas Gatos',
        ),
    ]
