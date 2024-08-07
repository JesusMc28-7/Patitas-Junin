# Generated by Django 5.0.6 on 2024-06-22 05:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0031_alter_adopcionesdb_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopcionesdb',
            name='Animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.resguardodb'),
        ),
        migrations.AlterField(
            model_name='resguardodb',
            name='Cuidador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resguardodb',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.animalesdb'),
        ),
        migrations.CreateModel(
            name='Fallecimientodb',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Id')),
                ('causa_muerte', models.TextField(max_length=100, verbose_name='Causas')),
                ('Fecha', models.DateField(verbose_name='Fecha de muerte')),
                ('Animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.resguardodb')),
            ],
            options={
                'verbose_name': 'Animales_Fallecidos',
                'db_table': 'Fallecimientos',
            },
        ),
    ]
