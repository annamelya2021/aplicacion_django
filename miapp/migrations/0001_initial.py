# Generated by Django 5.2.3 on 2025-06-18 11:37

import datetime
import django.db.models.deletion
import miapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('codigo_inventario', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('libro', 'Libro'), ('revista', 'Revista'), ('dvd', 'DVD')], max_length=10)),
                ('autor', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_paginas', models.IntegerField(blank=True, null=True)),
                ('fecha_publicacion', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_edicion', models.CharField(blank=True, max_length=255, null=True)),
                ('duracion', models.IntegerField(blank=True, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.CharField(default=miapp.models.generar_id_usuario, max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_prestamo', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_devolucion', models.DateTimeField(default=miapp.models.calcular_fecha_devolucion)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='miapp.material')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='miapp.usuario')),
            ],
            options={
                'verbose_name': 'Préstamo',
                'verbose_name_plural': 'Préstamos',
            },
        ),
    ]
