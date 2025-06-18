from django.db import models
import uuid
from datetime import datetime, timedelta

def generar_id_usuario():
    return uuid.uuid4().hex[:6].upper()

def calcular_fecha_devolucion():
    return datetime.now() + timedelta(days=14)

class Usuario(models.Model):
    id_usuario = models.CharField(
        primary_key=True,
        max_length=6,
        default=generar_id_usuario
    )
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Material(models.Model):
    TIPO_CHOICES = [
        ('libro', 'Libro'),
        ('revista', 'Revista'),
        ('dvd', 'DVD'),
    ]

    codigo_inventario = models.CharField(primary_key=True, max_length=255)
    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    autor = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)
    numero_paginas = models.IntegerField(null=True, blank=True)
    fecha_publicacion = models.CharField(max_length=255, null=True, blank=True)
    numero_edicion = models.CharField(max_length=255, null=True, blank=True)
    duracion = models.IntegerField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} ({self.codigo_inventario})"

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )
    fecha_prestamo = models.DateTimeField(default=datetime.now)
    fecha_devolucion = models.DateTimeField(default=calcular_fecha_devolucion)

    def __str__(self):
        return f"Préstamo {self.id} - {self.usuario} - {self.material}"

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
