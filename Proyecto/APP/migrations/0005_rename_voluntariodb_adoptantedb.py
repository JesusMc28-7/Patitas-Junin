# Generated by Django 5.0.6 on 2024-06-21 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_esterilizaciondb_generodb_tamañodb_voluntariodb_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voluntariodb',
            new_name='Adoptantedb',
        ),
    ]
