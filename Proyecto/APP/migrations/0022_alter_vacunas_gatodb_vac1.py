# Generated by Django 5.0.6 on 2024-06-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0021_alter_vacunas_gatodb_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacunas_gatodb',
            name='vac1',
            field=models.CharField(default=None, max_length=50, verbose_name='Giardiasis'),
        ),
    ]
