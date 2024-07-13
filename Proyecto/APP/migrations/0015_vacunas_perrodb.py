# Generated by Django 5.0.6 on 2024-06-21 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0014_alter_gatodb_id_alter_perrosdb_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='vacunas_perrodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.perrosdb', verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Vacunas_perro',
                'verbose_name_plural': 'Vacunas_perros',
                'db_table': 'Vacunas_Perros',
            },
        ),
    ]
